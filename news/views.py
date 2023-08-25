from django.shortcuts import render, redirect


from . import models
# Create your views here.
from django.contrib.auth.decorators import login_required
import random

def setContent(content):
    contents = []
    for item in content:
        content = {}
        content['id'] = item.id
        content['occupation'] = item.author.occupation
        content['author_desc'] = item.author.description
        content["author"] = models.Author.objects.get(id=item.author.id)
        content['author_profile'] = f"/media/{models.Author.objects.get(id=item.author.id).profile_img}"
        
        if models.Content.objects.get(id=item.id).poster =="" :
            content['poster'] = f"/media/{models.Category.objects.get(id=item.category.id).img}"
        else :
            content['poster'] = f"/media/{item.poster}"
        
        content["title"] = item.title[:20]
        content["description"] = item.description[:20]
        content["detail"] = item.detail
        content['category'] = item.category
        content["read"] = item.read
        content["write"] = item.write
        contents.append(content)
        
    return contents

def index(req):
    return redirect('feeds')


def feeds(req):
    context = {}
    # news = models.News.objects.all()
    context["author"] = models.Author.objects.all()
    
    contents = models.Content.objects.order_by("write")
    trends = models.Content.objects.order_by("read")[:3]

    context["topics"] = []
    context['trends'] = setContent(trends)
    context["last_content"] = setContent(contents)

    category = models.Category.objects.all()
    for cats in category:
        cat = {}
        cat['img'] = cats.img
        cat['category'] = cats.category
        cat['len'] = models.Content.objects.filter(category=models.Category.objects.get(id=cats.id)).count()
        
        context['topics'].append(cat)
    
    context["last_content"].reverse()
    context["last_content"][:4]
    
    return render(req, 'feeds.html', context)


def read(req, id):
    context= {}
    
    content = models.Content.objects.get(id=id)
    read = int(content.read)
    read += 1
    models.Content.objects.filter(id=id).update(read = read)
    context['author'] = models.Author.objects.get(id=content.author.id)
    con = content
    cont = {}
    cont['id'] = con.id
    if con.poster == "":
        cont['poster'] = f"/media/{models.Category.objects.get(id=con.category.id).img}"
        
    else :
        cont['poster'] = con.poster
    print(cont['poster'])
    cont['title'] = con.title
    cont['description'] = con.description
    cont['detail'] = con.detail
    cont['read'] = con.read
    cont['category'] = con.category
    cont['write'] = con.write
    
    
    context['content'] = cont
    
    related = models.Content.objects.filter(author=models.Author.objects.get(id=content.author.id))
    if related.count() < 3:
        context['related'] = setContent(related)
    else :  
        context['related'] = random.choices(setContent(related), k=3)
    
    
    
    
    
    
    return render(req, 'read.html' ,context)

def filter_author(request, id):
    context ={}
    author = models.Author.objects.get(id=id)
    
    content = models.Content.objects.filter(author=author)
    
    context["contents"] = setContent(content)
    context["author"] = author
    
    
    
    return render(request, 'filter_author.html', context)