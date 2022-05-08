from django.shortcuts import render
from django.views.generic import ListView, DetailView
from home.models import Post


# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home/home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'home/post_detail.html'
