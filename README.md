# Intelligent News Summarizer

An intelligent system that fetches news articles, processes them using a large language model (LLM), and provides analysis such as summarization, key point extraction, sentiment analysis, and topic classification. This project demonstrates API integration, prompt engineering, and data processing.

## Project Structure

```plaintext
intelligent-news-summarizer/
├── news_summarization/
│   ├── __init__.py
│   ├── news_api.py              # Handles fetching news articles from NewsAPI
│   ├── text_preprocessing.py     # Cleans and preprocesses text data
│   ├── llm_interactions.py       # Interactions with LLM for summarization, sentiment, etc.
│   ├── analysis.py               # Analysis functions like trending topics, sentiment tracking
│   ├── api.py                    # FastAPI endpoint setup
├── tests/
│   ├── test_news_api.py          # Unit tests for news_api module
│   ├── test_text_preprocessing.py # Unit tests for text_preprocessing module
│   ├── test_llm_interactions.py  # Unit tests for llm_interactions module
│   ├── test_analysis.py          # Unit tests for analysis module
├── .env.example                  # Template for environment variables
├── requirements.txt              # Project dependencies
├── README.md                     # Project documentation
├── run_tests.sh                  # Script to run tests

***Features***
-Fetches news articles from NewsAPI based on a search query.
-Processes and cleans news text data.
-Integrates with an LLM API (e.g., OpenAI) for:
    -Article summarization
    -Key points extraction
    -Sentiment analysis
    -Topic classification
-Provides insights such as trending topics, sentiment tracking, and topic clusters.
-FastAPI endpoint to expose functionality as an API.

***Getting Started***
Prerequisites
-Python 3.8 or later
-An API key for NewsAPI and OpenAI (or any supported LLM provider).

Setup
1. Clone the repository:
git clone https://github.com/your-username/intelligent-news-summarizer.git
cd intelligent-news-summarizer

2. Install dependencies:
pip install -r requirements.txt

3. Set up environment variables:

    -Copy the .env.example file to .env
    
    cp .env.example .env

    -Open .env and replace placeholders with your API keys.

Usage
1. Run the FastAPI server:

uvicorn news_summarization.api:app --reload

The API will be accessible at http://127.0.0.1:8000.

2. Send Requests:

-Access the API documentation at http://127.0.0.1:8000/docs for endpoints and usage.

3. Run Tests:

-Execute all unit tests with the following command:

./run_tests.sh


Example Endpoints
-GET /summarize: Summarizes fetched news articles.
-POST /analyze: Analyzes an article for sentiment, key points, and topic classification.

Environment Variables
Add your API keys to the .env file in the following format:

OPENAI_API_KEY=your_openai_api_key_here
NEWSDATA_API_KEY=your_newsdata_api_key_here


Additional Information
Modular Design
The project is structured into distinct modules, each handling a specific part of the pipeline:

-news_api.py: For fetching news articles.
-text_preprocessing.py: For cleaning and preprocessing text data.
-llm_interactions.py: For interacting with the LLM.
-analysis.py: For performing analysis and extracting insights.
-api.py: For exposing functionalities as API endpoints using FastAPI.

Testing
Unit tests are provided for all core modules in the tests/ directory. Tests can be run using pytest to ensure each module performs as expected.
    
40b71d2 (Initial commit for Intelligent News Summarizer project)
