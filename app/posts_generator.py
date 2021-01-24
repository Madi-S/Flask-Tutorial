import requests
from newsapi import NewsApiClient
from config import news_key


def get_posts(limit, q):
    newsapi = NewsApiClient(api_key=news_key)
    top_headlines = newsapi.get_top_headlines(q=q)['articles'][:limit]
    articles = []
    for headline in top_headlines:
        articles.append({
            'title': headline['title'],
            'body': headline['content']
        })
    return articles


if __name__ == '__main__':
    posts = get_posts(limit=20, q=None)
    for p in posts:
        print(len(p['title']))
