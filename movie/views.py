from django.shortcuts import render,get_object_or_404,redirect
from . import models
from . import forms
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def homepage(request):
    movies = models.Movies.objects.all()
    return render(request,'home.html',{'movies':movies})

def index(request):
    movies = models.Movies.objects.all()
    return render(request,'home.html',{'movies':movies})


def detail(request,id):
    movie = get_object_or_404(models.Movies,id=id)
    comments = models.Comments.objects.filter(movie=movie)
    if request.method=='POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.movie = movie
            new_comment.username = request.user
            new_comment.save()
            return redirect('detail',id=movie.id)
    else:
        comment_form = forms.CommentForm()
    return render(request,'detail.html',{'movie':movie,
                                         'comment':comments,
                                         'comment_form':comment_form})

def registration(request):
    if request.method == 'POST':
        form = forms.RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = forms.RegForm()
    return render(request,'reg.html',{'form':form})

def sign_in(request):
    if request.method == 'POST':
        form = forms.LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = forms.LoginForm()
    return render(request,'log_in.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('home')

