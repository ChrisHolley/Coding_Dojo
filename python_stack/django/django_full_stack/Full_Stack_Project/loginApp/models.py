from django.db import models
from datetime import datetime

# Create your models here.
# class userManager():
#     def new_user_validator(self, postData):
#         errors = {}
#         filter_duplicate_email = user.objects.filter(email=postData['email'])

class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birthday = models.DateField()
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # objects = userManager()