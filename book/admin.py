from django.contrib import admin

# Register your models here.

from .models import Destination, Featured_Destinations, Featured_Tours

admin.site.register(Destination)
admin.site.register(Featured_Destinations)
admin.site.register(Featured_Tours)