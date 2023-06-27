from django.urls import path
from . import views 

app_name = 'blog'

#Blog
urlpatterns = [
    path('', views.blog, name='home')

]
