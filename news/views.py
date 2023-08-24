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
    
    contents = models.Content.objects.order_by("write")
    trends = models.Content.objects.order_by("read")[:3]

    context["topics"] = []
    context['trends'] = []
    
    for item in trends:
        content = {}
        content['id'] = item.id
        content["author"] = models.Author.objects.get(id=item.author.id)
        content['occupation'] = item.author.occupation
        content['author_desc'] = item.author.description
        content['author_profile'] = f"media/{models.Author.objects.get(id=item.author.id).profile_img}"
        
        if models.Content.objects.get(id=item.id).poster =="" :
            content['poster'] = f"media/{models.Category.objects.get(id=item.category.id).img}"
        else :
            content['poster'] = f"media/{item.poster}"
        
        content["title"] = item.title[:20]
        content["description"] = item.description[:20]
        content["detail"] = item.detail
        
        content["read"] = item.read
        content["write"] = item.write
        context["trends"].append(content)
    
    for item in contents:
        content = {}
        content['id'] = item.id
        content['occupation'] = item.author.occupation
        content['author_desc'] = item.author.description
        content["author"] = models.Author.objects.get(id=item.author.id)
        content['author_profile'] = f"media/{models.Author.objects.get(id=item.author.id).profile_img}"
        
        if models.Content.objects.get(id=item.id).poster =="" :
            content['poster'] = f"media/{models.Category.objects.get(id=item.category.id).img}"
        else :
            content['poster'] = f"media/{item.poster}"
        
        content["title"] = item.title[:20]
        content["description"] = item.description[:20]
        content["detail"] = item.detail

        content["read"] = item.read
        content["write"] = item.write
        context["last_content"].append(content)
        
    
    category = models.Category.objects.all()
    for cats in category:
        cat = {}
        cat['img'] = cats.img
        cat['category'] = cats.category
        cat['len'] = models.Content.objects.filter(category=models.Category.objects.get(id=cats.id)).count()
        
        context['topics'].append(cat)
    
    context["last_content"].reverse()
    return render(req, 'index.html', context)







def read(req, id):
    context= {}
    content = models.Content.objects.get(id=id)
    context['content'] = models.Content.objects.get(id=id)
    context['author'] = models.Author.objects.get(id=content.author.id)
    
    
    
    
    return render(req, 'detail-page.html' ,context)