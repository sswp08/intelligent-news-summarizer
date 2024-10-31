# news_api.py

from newsdataapi import NewsDataApiClient
from time import sleep
import random
import requests

class NewsExtractor:
    """
    A class for extracting news articles from the NewsAPI with rate limiting and error handling.

    Attributes:
        api (NewsDataApiClient): API client for fetching news articles.
    """

    def __init__(self, api_key: str):
        """
        Initializes the NewsExtractor with an API key.

        Args:
            api_key (str): API key for NewsDataApiClient.
        """
        self.api = NewsDataApiClient(apikey=api_key)

    def get_news(self, query: str, country="in", language="en") -> list:
        """
        Fetches news articles based on a search query with error handling.

        Args:
            query (str): The search query for fetching news.
            country (str): Country code for the news source (default "in").
            language (str): Language code for the articles (default "en").

        Returns:
            list: A list of dictionaries containing article information.
        """
        try:
            response = self.api.news_api(q=query, country=country, language=language)
            articles = [
                {
                    'title': content.get('title', ''),
                    'date': content.get('pubDate', ''),
                    'source': content.get('source_id', ''),
                    'content': content.get('content', '')
                }
                for content in response.get('results', [])
            ]
            sleep(random.uniform(1, 2))  # Basic rate limiting
            return articles
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            return []
