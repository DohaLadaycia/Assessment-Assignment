from django.shortcuts import render
from .models import NewsArticle
from .forms import NewsFilterForm
from .utils import fetch_and_store_news

def news_list(request):
    form = NewsFilterForm(request.GET or None)
    category = request.GET.get('category')
    country = request.GET.get('country')
    
    fetch_and_store_news(category=category, country=country)
    
    articles = NewsArticle.objects.all()
    
    if category:
        articles = articles.filter(category=category)
    if country:
        articles = articles.filter(country=country)
    
    context = {
        'form': form,
        'articles': articles
    }
    return render(request, 'news_list.html', context)
