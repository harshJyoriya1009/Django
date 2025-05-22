from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class AppVarity(models.Model):
    APP_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GI', 'GINJER'),
        ('KI', 'KIWI'),
        ('EL', 'ELACHI'),
    ] 
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='apps/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE_CHOICE)
    description = models.TextField(default='')
    pricing = models.CharField(max_length=45, default='0')

    def __str__(self):
        return self.name
    
# One to Many
class AppReview(models.Model):
    app1 = models.ForeignKey(AppVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.app1.name}'


# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=400)
    location = models.CharField(max_length=400)
    app_varities = models.ManyToManyField(AppVarity, related_name='stores')

    def __str__(self):
        return self.name


# One to One 
class AppVerification(models.Model):
    app1 = models.OneToOneField(AppVarity, on_delete=models.CASCADE, related_name='verify')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()

    def __str__(self):
        return f'Verification for {self.name.app1}'
    

class AppBuying(models.Model):
    name = models.CharField(max_length=40)
    app1 = models.OneToOneField(AppVarity, on_delete=models.CASCADE, related_name='buying')
    buying = models.CharField(max_length=45, default='0')
    issue_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'You buy this app {self.name.app1}'
    
