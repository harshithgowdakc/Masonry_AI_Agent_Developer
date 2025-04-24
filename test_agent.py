#test_agent
import unittest
from unittest.mock import patch, MagicMock
from agent import WebResearchAgent

class TestWebResearchAgent(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment"""
        self.agent = WebResearchAgent()
        self.test_query = "AI advancements"
    
    @patch('agent.requests.get')
    def test_search(self, mock_get):
        """Test that search method returns expected results"""
        # Create mock response
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "organic_results": [
                {"title": "Test Result 1", "link": "https://example.com/1"},
                {"title": "Test Result 2", "link": "https://example.com/2"}
            ]
        }
        mock_get.return_value = mock_response
        
        # Call the search method
        results = self.agent.search(self.test_query)
        
        # Verify results
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["title"], "Test Result 1")
    
    def test_scrape_error_handling(self):
        """Test error handling in scrape method"""
        # Test with invalid URL to trigger error
        content = self.agent.scrape("https://nonexistent-site-123456.com")
        
        # Check that error handling works
        self.assertIn("Failed to scrape", content)
    
    @patch('agent.genai.GenerativeModel')
    def test_synthesize(self, mock_model_class):
        """Test the synthesize method"""
        # Create mock model and response
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Test research report"
        mock_model.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model
        
        # Reinitialize agent with mock model
        self.agent = WebResearchAgent()
        
        # Test sources
        sources = ["Test source 1", "Test source 2"]
        
        # Call synthesize method
        report = self.agent.synthesize(self.test_query, sources)
        
        # Verify report
        self.assertEqual(report, "Test research report")

if __name__ == "__main__":
    unittest.main()