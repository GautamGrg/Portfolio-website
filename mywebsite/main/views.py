from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home (request):
    return render (request, 'main/home.html')

# def posts (request):
#     return HttpResponse ('<h2>Posts</h2>')

# def post (request):
#     return HttpResponse ('<h2>Post title</h2>')

# def profile (request):
#     return HttpResponse ('<h2>User Profile</h2>')