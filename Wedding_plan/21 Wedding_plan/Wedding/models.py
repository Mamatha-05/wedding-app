from django.db import models
from django.contrib.auth.models import User
class Wedding(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=300)
    def __str__(self):
        return self.name
class Vendor(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    service = models.CharField(max_length=200)
    contact_info = models.TextField()

    def __str__(self):
        return self.name
class select(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    wedding=models.ForeignKey(Wedding, on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    status=models.TextField(default='pending')
    def __str__(self):
        return self.user.username
class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField()
    name=models.CharField(max_length=29)
    