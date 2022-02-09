from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path("posts", views.allPosts, name="posts-page"),
    path("posts/<slug:slug>", views.singlePost,
         name="post-detail-page"),
    path("thank_you", views.thank_you, name="thank_you"),
]