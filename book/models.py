from django.db import models

# Create your models here.

from django.db import models

class Destination(models.Model):
    # Example: "Rome, Italy"
    name = models.CharField(max_length=100)
    
    # Example: "The timeless city, where ancient ruins meet breathtaking Renaissance artistry."
    description = models.TextField()
    
    # Example: "assets/img/travel/destination-4.webp"
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    
    # Example: "Historic"
    tag = models.CharField(max_length=50)
    
    # Example: "18 Excursions"
    excursions = models.PositiveIntegerField(default=0)
    
    # Example: "1320" (USD)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Example: for filtering (cultural, adventure, beach, etc.)
    category = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Featured_Destinations(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='featured_destinations/', blank=True, null=True)
    ratings = models.DecimalField(max_digits=3, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expeditions = models.PositiveIntegerField(default=0)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.name

