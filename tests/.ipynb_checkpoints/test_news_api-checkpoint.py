# tests/test_news_api.py

import pytest
from news_summarization.news_api import NewsExtractor

# Mock the API key
API_KEY = "mock_api_key"

@pytest.fixture
def news_extractor():
    """Fixture for creating a NewsExtractor instance."""
    return NewsExtractor(api_key=API_KEY)

def test_get_news(news_extractor, mocker):
    """Test fetching news articles."""
    # Mock the API response
    mock_response = {
        "results": [
            {
                "title": "Sample News Title",
                "pubDate": "2023-10-31",
                "source_id": "sample_source",
                "content": "Sample news content for testing."
            }
        ]
    }
    
    mocker.patch.object(news_extractor.api, 'news_api', return_value=mock_response)
    
    articles = news_extractor.get_news("sample query")
    
    # Check if articles are fetched and parsed correctly
    assert len(articles) == 1
    assert articles[0]["title"] == "Sample News Title"
    assert articles[0]["date"] == "2023-10-31"
    assert articles[0]["source"] == "sample_source"
    assert articles[0]["content"] == "Sample news content for testing."
