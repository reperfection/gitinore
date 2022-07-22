from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm, CommentForm, HashTagForm
from django.utils import timezone
from .models import Blog, Comment, HashTag
from django.http import request

# Create your views here.
def index(request):
    return render(request, 'index.html')
def create(request, blog = None):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            form.save_m2m()
            return redirect('index')
    else:
        form = BlogForm (instance = blog)
        return render(request, 'create.html', {'form':form})
    
def read(request):
    blogs = Blog.objects
    return render(request, 'read.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST" :
        form = CommentForm(request.POST)
        if form.is_valid() :
            comment = form.save(commit = False)
            comment.blog_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail', id)
        
    else:
        form = CommentForm()
        return render(request, 'detail.html', {'blog':blog, 'form':form})

def edit(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'edit.html', {'form':form})
    
def delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('read')

def hashtag(request, hashtag = None):
    if request.method == "POST" :
        form = HashTagForm(request.POST, instance = hashtag)
        if form.is_valid() :
            hashtag = form.save(commit = False)
            if HashTag.objects.filter(name=form.cleaned_data['name']) :
                form = HashTagForm()
                error_message = "이미 존재하는 해시태그 입니다"
                return render(request, 'hashtag.html', {'form':form, "error_message":error_message})
            else :
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('read')
    else :
        form = HashTagForm(instance = hashtag)
        return render (request, 'hashtag.html', {'form':form}) 