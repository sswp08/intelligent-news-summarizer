# tests/test_api.py

import pytest
from fastapi.testclient import TestClient
from news_summarization.api import app
from unittest.mock import patch

client = TestClient(app)

@pytest.fixture
def mock_news_data():
    """Mock data for news articles."""
    return [
        {
            "title": "Sample News Title",
            "date": "2023-10-31",
            "source": "sample_source",
            "content": "Sample news content for testing."
        }
    ]

@pytest.fixture
def mock_summaries():
    """Mock data for summaries returned by LLM."""
    return ["This is a summary of the article."]

@pytest.fixture
def mock_topics():
    """Mock data for topics."""
    return ["Technology"]

@pytest.fixture
def mock_sentiments():
    """Mock data for sentiments."""
    return ["Positive"]

@pytest.fixture
def mock_trending_topics():
    """Mock data for trending topics."""
    return [("Technology", 3)]

@pytest.fixture
def mock_sentiment_trends():
    """Mock data for sentiment trends."""
    return {"Positive": 3, "Neutral": 1}

@pytest.fixture
def mock_clusters():
    """Mock data for clusters."""
    return {
        "0": ["This is a summary of the article."],
        "1": ["Another summary for a different article."]
    }

def test_process_query_endpoint(
    mocker, mock_news_data, mock_summaries, mock_topics, 
    mock_sentiments, mock_trending_topics, mock_sentiment_trends, mock_clusters
):
    """Test the /process_query/ endpoint."""
    
    # Mock dependencies within the endpoint
    mocker.patch('news_summarization.news_api.NewsExtractor.get_news', return_value=mock_news_data)
    mocker.patch('news_summarization.llm_interactions.generate_summary', side_effect=mock_summaries)
    mocker.patch('news_summarization.llm_interactions.classify_topic', side_effect=mock_topics)
    mocker.patch('news_summarization.llm_interactions.analyze_sentiment', side_effect=mock_sentiments)
    mocker.patch('news_summarization.analysis.identify_trending_topics', return_value=mock_trending_topics)
    mocker.patch('news_summarization.analysis.track_sentiment', return_value=mock_sentiment_trends)
    mocker.patch('news_summarization.analysis.generate_clusters', return_value=mock_clusters)
    
    # Define a request payload
    payload = {
        "query": "technology",
        "total_news": 1
    }
    
    # Make a POST request to the /process_query/ endpoint
    response = client.post("/process_query/", json=payload)
    
    # Assert that the response is successful
    assert response.status_code == 200
    
    # Check if the response contains the expected keys
    response_data = response.json()
    assert "summaries" in response_data
    assert "topics" in response_data
    assert "sentiments" in response_data
    assert "trending_topics" in response_data
    assert "sentiment_trends" in response_data
    assert "clusters" in response_data
    
    # Assert that the returned data matches the mock data
    assert response_data["summaries"] == mock_summaries
    assert response_data["topics"] == mock_topics
    assert response_data["sentiments"] == mock_sentiments
    assert response_data["trending_topics"] == mock_trending_topics
    assert response_data["sentiment_trends"] == mock_sentiment_trends
    assert response_data["clusters"] == mock_clusters
