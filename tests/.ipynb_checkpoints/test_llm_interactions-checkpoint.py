# tests/test_llm_interactions.py

import pytest
from news_summarization.llm_interactions import generate_summary, extract_key_points, analyze_sentiment, classify_topic

API_KEY = "mock_openai_key"

def test_generate_summary(mocker):
    """Test LLM-based summary generation."""
    mocker.patch("openai.ChatCompletion.create", return_value={
        'choices': [{'message': {'content': 'This is a summary of the article.'}}]
    })
    content = "Long article content for testing."
    summary = generate_summary(content, 50, API_KEY)
    
    # Check if summary is generated and is within limit
    assert isinstance(summary, str)
    assert len(summary) <= 50
    assert summary == "This is a summary of the article."

def test_extract_key_points(mocker):
    """Test LLM-based key point extraction."""
    mocker.patch("openai.ChatCompletion.create", return_value={
        'choices': [{'message': {'content': 'Key points extracted from the content.'}}]
    })
    key_points = extract_key_points("Article content.", API_KEY)
    
    # Check if key points are correctly returned
    assert key_points == "Key points extracted from the content."

def test_analyze_sentiment(mocker):
    """Test LLM-based sentiment analysis."""
    mocker.patch("openai.ChatCompletion.create", return_value={
        'choices': [{'message': {'content': 'Positive sentiment detected.'}}]
    })
    sentiment = analyze_sentiment("Positive article content.", API_KEY)
    
    # Check if sentiment is correctly analyzed
    assert sentiment == "Positive sentiment detected."

def test_classify_topic(mocker):
    """Test LLM-based topic classification."""
    mocker.patch("openai.ChatCompletion.create", return_value={
        'choices': [{'message': {'content': 'Technology'}}]
    })
    topic = classify_topic("Article about tech innovations.", API_KEY)
    
    # Check if topic is correctly classified
    assert topic == "Technology"
