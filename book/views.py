from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'book/index.html')

def about(request):
    return render(request, 'book/about.html')

def destinations(request):
    return render(request, 'book/destinations.html')

def tours(request):
    return render(request, 'book/tours.html')

def gallery(request):
    return render(request, 'book/gallery.html')

def contact(request):
    return render(request, 'book/contact.html')
