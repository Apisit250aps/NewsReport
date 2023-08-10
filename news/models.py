from django.db import models

# Create your models here.

PREFIXES = (
    (1, 'นาย'),
    (2,'นางสาว'),
    (3,'นาง'),
)

class Writer(models.Model):
    prfix = models.IntegerField(choices=PREFIXES)
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Category(models.Model):
    category = models.CharField(max_length=128)
    
    def __str__(self):
        return self.category
    


class News(models.Model):
    
    title = models.CharField(max_length=128)
    detail = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_by = models.ForeignKey(Writer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}, {self.post_by}"    
    
