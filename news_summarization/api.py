# api.py

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from news_api import NewsExtractor
from text_preprocessing import preprocess_text
from llm_interactions import generate_summary, extract_key_points, analyze_sentiment, classify_topic
from analysis import identify_trending_topics, track_sentiment, generate_clusters
import os
import asyncio

# Load environment variables from .env file
load_dotenv()

# Access API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    total_news: int = 5

@app.post("/process_query/")
async def process_query(request: QueryRequest):
    """
    Endpoint to process a query and return processed results with analysis.

    Args:
        request (QueryRequest): Request payload with query and total_news count.

    Returns:
        dict: Results including summaries, key points, sentiments, topics, and analysis.
    """
    news_extractor = NewsExtractor(api_key=NEWSDATA_API_KEY)
    articles = news_extractor.get_news(query=request.query)

    # Asynchronous LLM tasks for improved performance
    tasks = [
        asyncio.create_task(generate_summary(article['content'], 175, OPENAI_API_KEY))
        for article in articles[:request.total_news]
    ]
    summaries = await asyncio.gather(*tasks)

    # Analysis tasks for trending topics, sentiments, and clusters
    topics = [classify_topic(article['content'], OPENAI_API_KEY) for article in articles]
    sentiments = [analyze_sentiment(article['content'], OPENAI_API_KEY) for article in articles]

    trending_topics = identify_trending_topics(topics)
    sentiment_trends = track_sentiment(sentiments)
    clusters = generate_clusters(summaries)

    return {
        "summaries": summaries,
        "topics": topics,
        "sentiments": sentiments,
        "trending_topics": trending_topics,
        "sentiment_trends": sentiment_trends,
        "clusters": clusters
    }
