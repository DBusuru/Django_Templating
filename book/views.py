from django.shortcuts import render

# Create your views here.
from .models import Destination, Featured_Destinations, Featured_Tours, Testimonial


def index(request):
    featured_destinations = Featured_Destinations.objects.all()
    context = {
        'featured_destinations': featured_destinations,
        'featured_tours': Featured_Tours.objects.all(),
        'testimonials': Testimonial.objects.all(),  # Placeholder for testimonials if needed
    }
    return render(request, 'book/index.html', context)


def about(request):
    return render(request, 'book/about.html')


def destinations(request):
    """Render the destinations page with a queryset of Destination objects.

    Admin-created Destination instances will appear in the template via the
    `destinations` context variable.
    """
    qs = Destination.objects.all()
    context = {
        'destinations': qs,
    }
    return render(request, 'book/destinations.html', context)


def tours(request):
    return render(request, 'book/tours.html')


def gallery(request):
    return render(request, 'book/gallery.html')


def contact(request):
    return render(request, 'book/contact.html')
