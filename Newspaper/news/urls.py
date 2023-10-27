from django.urls import path, include
#from .views import PostsList
from news.views import NewsList, PostDetail

app_name = 'news'

urlpatterns = [
    #path('admin/', admin.site.urls), 
    path('posts/', NewsList.as_view()), 
    path('<int:pk>', PostDetail.as_view()),]