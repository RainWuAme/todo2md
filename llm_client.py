import os
from typing import TypedDict, List
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

# Configuration
# User's vLLM endpoint
VLLM_BASE_URL = os.environ.get("VLLM_BASE_URL", "http://localhost:8000/v1")
# Model name might need to match what vLLM is serving
VLLM_MODEL_NAME = os.environ.get("VLLM_MODEL_NAME", "hosted_vllm/model")
# API Key is usually ignored by vLLM but required by the client
VLLM_API_KEY = os.environ.get("VLLM_API_KEY", "EMPTY")

class TaskState(TypedDict):
    tasks_text: str
    summary: str

def generate_summary(tasks_text: str) -> str:
    """
    Generates a structured summary of the tasks using a local vLLM via LangGraph.
    """
    
    # Define the LLM
    llm = ChatOpenAI(
        base_url=VLLM_BASE_URL,
        api_key=VLLM_API_KEY,
        model=VLLM_MODEL_NAME,
        temperature=0.7
    )
    
    # Define the node
    def summarize_node(state: TaskState):
        prompt = f"""
        You are a helpful assistant that summarizes completed tasks for a weekly report.
        Here is a list of completed tasks:
        
        {state['tasks_text']}
        
        Please rewrite this list into a more structured, human-readable format for a weekly report.
        - Group related tasks together if possible.
        - Use bullet points.
        - Be concise but descriptive.
        - The output should be valid Markdown.
        - Do not include any preamble, just the markdown content.
        """
        
        try:
            response = llm.invoke(prompt)
            return {"summary": response.content}
        except Exception as e:
            print(f"Error invoking vLLM: {e}")
            return {"summary": f"Error generating summary: {e}\n\nOriginal tasks:\n{state['tasks_text']}"}

    # Build the graph
    workflow = StateGraph(TaskState)
    workflow.add_node("summarize", summarize_node)
    workflow.set_entry_point("summarize")
    workflow.add_edge("summarize", END)
    
    app = workflow.compile()
    
    # Run the graph
    result = app.invoke({"tasks_text": tasks_text, "summary": ""})
    return result.get("summary", "")

class WeeklyReportItem(TypedDict):
    target_file: str
    content: str

class WeeklyReportOutput(TypedDict):
    main_summary: str
    file_updates: List[WeeklyReportItem]

def process_weekly_tasks(tasks_text: str, available_files: List[str]) -> WeeklyReportOutput:
    """
    Processes tasks to generate a weekly report summary and categorize items into specific files.
    """
    from langchain_core.output_parsers import JsonOutputParser
    from langchain_core.prompts import PromptTemplate
    from pydantic import BaseModel, Field

    # Define Pydantic model for structured output
    class ReportItem(BaseModel):
        target_file: str = Field(description="The filename to update (must be one of the available files)")
        content: str = Field(description="The content to append to the target file (bullet points)")

    class ReportOutput(BaseModel):
        main_summary: str = Field(description="A concise summary sentence for the main research log")
        file_updates: List[ReportItem] = Field(description="List of updates for specific files")

    parser = JsonOutputParser(pydantic_object=ReportOutput)

    llm = ChatOpenAI(
        base_url=VLLM_BASE_URL,
        api_key=VLLM_API_KEY,
        model=VLLM_MODEL_NAME,
        temperature=0.1
    )

    prompt = PromptTemplate(
        template="""You are a helpful assistant that prepares weekly research reports.
        
        Here is the list of tasks completed this week:
        {tasks_text}
        
        Available target files for detailed logs:
        {available_files}
        
        Your goal is to:
        1. Select progress items suitable for showing results in a weekly meeting (ignore minor admin tasks unless relevant).
        2. Group these items and assign them to the most appropriate target file from the list.
        3. Generate a concise summary sentence for the main 'Research_Log_Refining_PKNs_with_LLMs.md'.
        
        Format instructions:
        {format_instructions}
        """,
        input_variables=["tasks_text", "available_files"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    chain = prompt | llm | parser

    try:
        response = chain.invoke({"tasks_text": tasks_text, "available_files": available_files})
        return response
    except Exception as e:
        print(f"Error processing weekly tasks: {e}")
        return {"main_summary": "Error generating report", "file_updates": []}
