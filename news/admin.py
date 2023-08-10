from django.contrib import admin

# Register your models here.

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = list_display
    
@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'post_by',
        'post_date',
    )


@admin.register(models.Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = (
        'prfix',
        'fname',
        'lname',
    )