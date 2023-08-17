from django.shortcuts import render, redirect


from . import models
# Create your views here.
from django.contrib.auth.decorators import login_required



def index(req):
    return redirect('feeds')


def feeds(req):
    # news = models.News.objects.all()
    
    return render(req, 'index.html', {
        "author":models.Author.objects.all(),
    })