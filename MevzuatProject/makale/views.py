from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from .forms import ArticleForm
import requests
from bs4 import BeautifulSoup

def download_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    title = soup.find('h1', class_='svTitle').text.strip()
                    content = soup.find('div', class_='Body').text.strip()
                    article = Article.objects.create(url=url, title=title, content=content)
                    messages.success(request, f'Makale başarıyla indirildi: {article.title}')
                else:
                    messages.error(request, f'Makale indirilemedi: İstek durumu {response.status_code}')
            except Exception as e:
                messages.error(request, f'Makale indirilemedi: {e}')
            return redirect('makale')
    else:
        form = ArticleForm()
    return render(request, 'makale.html', {'form': form})
