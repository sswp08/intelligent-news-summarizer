# tests/test_text_preprocessing.py

import pytest
from news_summarization.text_preprocessing import preprocess_text

def test_preprocess_text():
    """Test text preprocessing function."""
    raw_text = "<html><body>Test content with HTML tags! & special characters!!!</body></html>"
    cleaned_text = preprocess_text(raw_text)
    
    # Check if HTML tags and special characters are removed correctly
    assert cleaned_text == "Test content with HTML tags special characters"
