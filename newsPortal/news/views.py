from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is the index page.")

from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news = News.objects.all().order_by('-publication_date')
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news_detail.html', {'news': news})
