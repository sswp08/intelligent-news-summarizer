# analysis.py

from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def identify_trending_topics(topics: list) -> list:
    """
    Identifies the top trending topics from the list of topics.

    Args:
        topics (list): List of topics from articles.

    Returns:
        list: Most common topics and their counts.
    """
    return Counter(topics).most_common(5)

def track_sentiment(sentiments: list) -> dict:
    """
    Tracks sentiment trends over time.

    Args:
        sentiments (list): List of sentiment labels.

    Returns:
        dict: Sentiment distribution.
    """
    return Counter(sentiments)

def generate_clusters(texts: list, num_clusters=3) -> dict:
    """
    Groups similar texts into clusters using TF-IDF and KMeans.

    Args:
        texts (list): List of texts to cluster.
        num_clusters (int): Number of clusters to generate.

    Returns:
        dict: Clusters with text grouped by similarity.
    """
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(texts)
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(vectors)
    clusters = {i: [] for i in range(num_clusters)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(texts[idx])
    return clusters
