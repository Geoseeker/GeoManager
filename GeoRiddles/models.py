from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Mystery(models.Model):
    name = models.CharField(max_length=64)
    gc_code = models.CharField(max_length=16)
    description = models.TextField()
    location = models.CharField(max_length = 64)
    image = models.ImageField(upload_to='GeoRiddles/static/', blank=True)
#     latitude = models.DecimalField(max_digits = 8, decimal_places = 6, null = True) #N or S
#     longitude = models.DecimalField(max_digits = 8, decimal_places = 6, null = True) #W or E
    added_by = models.ForeignKey(User, default=1)
    
    def get_absolute_url(self):
        return reverse('geospot', kwargs={'id': self.id})
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mystery Cache'  
        verbose_name_plural = 'Mysterki'
