import unittest
from unittest.mock import patch, MagicMock
from llm_client import generate_summary

class TestLLMClient(unittest.TestCase):
    
    @patch('llm_client.ChatOpenAI')
    @patch('llm_client.StateGraph')
    def test_generate_summary(self, mock_state_graph, mock_chat_openai):
        # Mock the graph app
        mock_app = MagicMock()
        mock_app.invoke.return_value = {"summary": "Mocked Summary"}
        
        # Mock the workflow compilation
        mock_workflow = MagicMock()
        mock_workflow.compile.return_value = mock_app
        mock_state_graph.return_value = mock_workflow
        
        # Run the function
        result = generate_summary("- Task 1")
        
        # Verify
        self.assertEqual(result, "Mocked Summary")
        mock_app.invoke.assert_called_once()
        print("Test passed: generate_summary called graph and returned result.")

if __name__ == '__main__':
    unittest.main()
