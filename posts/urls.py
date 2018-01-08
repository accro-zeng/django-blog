from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>', views.detail, name='detail'),
    path('archives', views.archives, name='archives'),
    path('category/<int:id>', views.category, name='category'),
    path('about', views.about, name='about')
]
