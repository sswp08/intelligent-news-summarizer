# tests/test_analysis.py

import pytest
from news_summarization.analysis import identify_trending_topics, track_sentiment, generate_clusters

def test_identify_trending_topics():
    """Test trending topic identification."""
    topics = ["Tech", "Health", "Tech", "Tech", "Finance", "Health"]
    trending = identify_trending_topics(topics)
    
    # Check if trending topics are correctly identified
    assert len(trending) == 3
    assert trending[0][0] == "Tech"
    assert trending[0][1] == 3

def test_track_sentiment():
    """Test sentiment tracking."""
    sentiments = ["Positive", "Negative", "Positive", "Neutral", "Positive"]
    sentiment_trends = track_sentiment(sentiments)
    
    # Check if sentiment trends are correctly tracked
    assert sentiment_trends["Positive"] == 3
    assert sentiment_trends["Negative"] == 1
    assert sentiment_trends["Neutral"] == 1

def test_generate_clusters():
    """Test text clustering."""
    texts = ["This is about technology.", "Health and wellness content.", "More on technology and gadgets."]
    clusters = generate_clusters(texts, num_clusters=2)
    
    # Check if clustering returns the expected number of clusters
    assert len(clusters) == 2
    assert all(isinstance(cluster, list) for cluster in clusters.values())
