from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog


# Create your views here.

def home(r):
    blogs = Blog.objects
    return render(r, 'home.html', {'blogs': blogs})



def detail(r, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(r, 'detail.html', {'details': details})



def new(r):
    return render(r, 'new.html')

def create(r):
    blog = Blog()
    blog.title = r.GET['title']
    blog.body = r.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))
