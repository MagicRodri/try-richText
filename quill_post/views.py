from django.shortcuts import render
from .forms import QPostForm
from .models import QPost

# Create your views here.

def create_post(request):
    return render(request,'create.html',{'form': QPostForm()})

def home(request):
    posts = QPost.objects.all()
    return render(request,'home.html',{'posts' : posts})