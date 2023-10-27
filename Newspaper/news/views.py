from django.views import generic
from django.views.generic import ListView, DetailView #Позволяет выводить объекты из базы данных в html
from .models import Post, Category
"""
class PostsList(ListView):
    model = Post 
    template_name = 'news_page.html'
    context_object_name = 'news'
"""

class NewsList(generic.ListView):
    """Представление главной страницы, которая отображает список всех новостей"""
    model = Post
    context_object_name = 'posts'
    template_name = 'tempates/flatpages/news_page.html'
    queryset = Post.objects.all().order_by('-dateCreation')

class PostDetail(DetailView):
    model = Post
    template_name = 'tempates/flatpages/post.html'
    context_object_name = 'post'
