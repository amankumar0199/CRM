from django.db import models
from django.urls import reverse
# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length = 20)
    Working_in = models.CharField(max_length = 20)
    Followups = models.TextField()

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('home')

class Activity(models.Model):
    ActivityName = models.CharField(max_length = 20)
    FromDate = models.CharField(max_length = 10)
    ToDate = models.CharField(max_length = 10)
    Venue = models.CharField(max_length = 30)
    Country = models.CharField(max_length = 20)
    State = models.CharField(max_length = 21)
    District = models.CharField(max_length = 40)
    Village_Panchayat = models.CharField(max_length = 40)
    ActivityDescription = models.TextField()
    def __str__(self):
        return self.ActivityName.upper()
