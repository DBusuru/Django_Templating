from django.contrib import admin

# Register your models here.

from .models import Destination, Featured_Destinations, Featured_Tours, Testimonial, Tour

admin.site.register(Destination)
admin.site.register(Featured_Destinations)
admin.site.register(Featured_Tours)
admin.site.register(Testimonial)
admin.site.register(Tour)
# Registering the models with the Django admin site allows for easy management of these models through the admin interface.
# This includes adding, editing, and deleting instances of these models without needing to write custom views or forms.