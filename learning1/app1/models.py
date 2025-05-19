from django.db import models
from django.utils import timezone

# Create your models here.
class AppVarity(models.Model):
    APP_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GI', 'GINJER'),
        ('KI', 'KIWI'),
    ] 
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='apps/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE_CHOICE)

