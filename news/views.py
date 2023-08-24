from django.shortcuts import render, redirect


from . import models
# Create your views here.
from django.contrib.auth.decorators import login_required
import random


def index(req):
    return redirect('feeds')


def feeds(req):
    context = {}
    # news = models.News.objects.all()
    context["last_content"] = []
    context["author"] = models.Author.objects.all()
    
    contents = random.choices(models.Content.objects.all(), k=2)
    trends = models.Content.objects.order_by("read")[:3]
    print(contents)
    context["topic"] = []
    context['trends'] = []
    
    for item in trends:
        content = {}
        content['id'] = item.id
        content["author"] = models.Author.objects.get(id=item.author.id)
        content['author_profile'] = f"media/{models.Author.objects.get(id=item.author.id).profile_img}"
        content['poster'] = f"media/{item.poster}"
        content["title"] = item.title[:25]
        content["description"] = item.description[:50]
        content["detail"] = item.detail
        content["like"] = item.like
        content["read"] = item.read
        content["write"] = item.write
        context["trends"].append(content)
    
    for item in contents:
        content = {}
        content['id'] = item.id
        content["author"] = models.Author.objects.get(id=item.author.id)
        content['author_profile'] = f"media/{models.Author.objects.get(id=item.author.id).profile_img}"
        content['poster'] = f"media/{item.poster}"
        content["title"] = item.title[:25]
        content["description"] = item.description[:50]
        content["detail"] = item.detail
        content["like"] = item.like
        content["read"] = item.read
        content["write"] = item.write
        context["last_content"].append(content)
        
    for t in random.choices(models.Category.objects.all(), k=4):
        topic = {}
        topic["topic"] = t.category
        topic['len'] = models.Author.objects.filter(category=models.Category.objects.get(id=t.id))
        print(topic['len'])
        
    
    context["last_content"].reverse()
    return render(req, 'index.html', context)

def read(req, id):
    context= {}
    content = models.Content.objects.get(id=id)
    context['content'] = models.Content.objects.get(id=id)
    context['author'] = models.Author.objects.get(id=content.author.id)
    
    
    
    
    return render(req, 'detail-page.html' ,context)