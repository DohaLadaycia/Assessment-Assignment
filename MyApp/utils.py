import requests
from .models import NewsArticle
#My KEY 
NEWS_API_KEY = '8743785a2f774f68bf1ee6ba51cec9be'  

def fetch_and_store_news(category=None, country=None):
    # Select 'top-headlines' (url)
    url = 'https://newsapi.org/v2/top-headlines'  
    params = {
        'apiKey': NEWS_API_KEY,
        'category': category or 'general',
        'country': country or 'us',
        'pageSize': 100  
    }
    

    response = requests.get(url, params=params)
    data = response.json()


    for article in data.get('articles', []):
        NewsArticle.objects.update_or_create(
            title=article['title'],
            defaults={
                'description': article.get('description', ''),  
                'published_at': article.get('publishedAt'),
                'url': article.get('url'),
                'category': category ,
                'country': country 
            }
        )
