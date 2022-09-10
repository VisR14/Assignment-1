from django.db import models


class User(models.Model):
    First_name = models.CharField(max_length = 180)
    Last_name = models.CharField(max_length = 180)
    email = models.EmailField(max_length = 250, unique = True)
    Mobile_number = models.CharField(max_length = 15, unique = True)
    

class Customer(models.Model):
    User = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    profile_number = models.CharField(max_length = 10)
    
    
    def __str__(self):
        return self.profile_number
# Create your models here.
