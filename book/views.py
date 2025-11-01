from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'book/index.html')

def about(request):
    return render(request, 'book/about.html')
