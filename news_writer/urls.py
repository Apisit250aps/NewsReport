"""
URL configuration for news_writer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from news import views as page

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', page.index, name='index'),
    path('feeds', page.feeds, name='feeds'),
    path('read/<int:id>', page.read, name='read'),
    path('filter-author/<int:id>', page.filter_author, name='filter-author'),
    path('filter-category/<int:id>', page.filter_category, name='filter-category')
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)