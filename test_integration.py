import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add current dir to path
sys.path.append("/Users/wuy/Projects/todo2md")

from update_wiki import update_home_md, HOME_MD_PATH

class TestUpdateWiki(unittest.TestCase):
    
    def setUp(self):
        # Backup Home.md
        if os.path.exists(HOME_MD_PATH):
            with open(HOME_MD_PATH, 'r') as f:
                self.original_content = f.read()
        else:
            self.original_content = ""
            
    def tearDown(self):
        # Restore Home.md
        with open(HOME_MD_PATH, 'w') as f:
            f.write(self.original_content)

    @patch('update_wiki.get_recently_completed_tasks')
    @patch('update_wiki.generate_summary')
    def test_update_home_md(self, mock_generate_summary, mock_get_tasks):
        # Mock tasks
        mock_get_tasks.return_value = {
            "Test Project": [
                {"text": "Task 1", "id": "1"},
                {"text": "Task 2", "id": "2"}
            ]
        }
        
        # Mock LLM response
        mock_generate_summary.return_value = "- Task 1 and Task 2 were completed.\n- They were great."
        
        # Run update
        update_home_md()
        
        # Check if Home.md was updated
        with open(HOME_MD_PATH, 'r') as f:
            content = f.read()
            
        self.assertIn("### Test Project", content)
        self.assertIn("- Task 1 and Task 2 were completed.", content)
        print("\nTest passed: Home.md updated with mock summary.")

if __name__ == '__main__':
    unittest.main()
