from django.shortcuts import render, redirect


from . import models
# Create your views here.

def inex(req):
    return redirect('feeds')

def feeds(req):
    news = models.News.objects.all()
    
    return render(req, 'feeds.html', {
        "news":news,
    })