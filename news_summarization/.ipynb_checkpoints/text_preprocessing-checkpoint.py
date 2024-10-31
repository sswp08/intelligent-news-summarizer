# text_preprocessing.py

import re
from bs4 import BeautifulSoup

def preprocess_text(text: str) -> str:
    """
    Cleans and normalizes text by removing HTML tags and special characters.

    Args:
        text (str): Raw text to be processed.

    Returns:
        str: Cleaned and preprocessed text.
    """
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()
    # Remove special characters and excess spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
