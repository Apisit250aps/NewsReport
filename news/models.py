from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=128)
    
    def __str__(self):
        return self.category
        
    
class Author(models.Model):
    
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile')
    occupation = models.CharField(max_length=128)
    
    follower = models.IntegerField()
    description = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    verify = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class Content(models.Model):
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    poster = models.ImageField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=150)
    detail = models.TextField()
    like = models.IntegerField()
    read = models.IntegerField()
    
    def __str__(self):
        return self.author
    
    
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
    link = models.IntegerField()
    
    def __str__(self):
        return self.user