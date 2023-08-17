from django.contrib import admin

# Register your models here.

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category'
    ]
    search_fields = [
        'category'
    ]
    
@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'user',
    ]

@admin.register(models.Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'title',
        
    ]

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'content',
    ]
    
    search_fields = [
        'user',
        'content',
    ]

@admin.register(models.ReplyComment)
class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'comment',
    ]
    
    search_fields = list_display