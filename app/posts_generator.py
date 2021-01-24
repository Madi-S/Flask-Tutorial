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
            'body': headline['content'],
            'created': headline['publishedAt']
        })
    return articles


if __name__ == '__main__':
    print(get_posts(limit=1, q='Chelsea'))
