from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    img = models.ImageField(upload_to='category', max_length=255)
    category = models.CharField(max_length=128)
    
    def __str__(self):
        return self.category

class Author(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile', max_length=255)
    occupation = models.CharField(max_length=128, default="-", null=True, blank=True)
    description = models.CharField(max_length=150, default="-", null=True, blank=True)
    verify = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class Follow(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow_date = models.DateTimeField(auto_now_add=True)

class Content(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='content', max_length=255, null=True, blank=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=150)
    detail = models.TextField()
    read = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    write = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Like(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} has like {self.content}"
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    detail = models.TextField()
    like = models.IntegerField()
    
    def __str__(self):
        return self.user

class ReplyComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    detail = models.TextField()
    like = models.IntegerField()
    
    def __str__(self):
        return self.user
    
