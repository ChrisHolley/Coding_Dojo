from django.db import models
from datetime import datetime
import re

class userManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        filter_email = user.objects.filter(email=postData['form_email'])
        if len(filter_email) > 0:
            errors['email_taken'] = "An account with this email already exists"
        if len(postData['form_first_name']) < 2:
            errors["name_length"] = "First name should be at least 2 characters"
        if len(postData['form_last_name']) < 2:
            errors["name_length"] = "Last name should be at least 2 characters"
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['form_email']):
            errors["invalid_email"] = "Not a valid email"
        if postData['form_password'] != postData['form_confirm_pw']:
            errors["confirm_password"] = "Passwords do not match"
        elif len(postData['form_password']) < 8:
            errors["password_length"] = "Passwords must be at least 8 characters"
            #convert date time from a string to a number
            # make sure release date is in the past
        try:    
            if datetime.strptime(postData['form_birthday'], "%Y-%m-%d") > datetime.now():
                errors['no_future_birth'] = "Cannot enter a future date for birth date"
        except:
                errors['empty_birthday'] = "Birth date required"
        return errors

    def login_validator(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['login_email']) < 3:
            errors["invalid_email"] = "Not a valid email"
        elif not email_regex.match(postData['login_email']):
            errors["invalid_email"] = "Not a valid email"
        return errors
class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birthday = models.DateField()
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = userManager()