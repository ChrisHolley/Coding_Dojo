from django.db import models
from datetime import datetime
class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        NameOfAllShows = Show.objects.filter(show_title=postData['form_title'])

        if len(NameOfAllShows) > 0:
            errors['name_taken'] = "Show already exists"
        if len(postData['form_title']) < 2:
            errors["title_length"] = "Blog name should be at least 2 characters"
        elif len(postData['form_title']) > 45:
            errors["title_length"] = "Blog name should be less than 46 characters"
        if len(postData['form_network']) < 2:
            errors["network_length"] = "Blog name should be at least 2 characters"
        elif len(postData['form_network']) > 15:
            errors["network_length"] = "Blog name should be less than 16 characters"
            #convert date time from a string to a number
            # make sure release date is in the past
        try:    
            if datetime.strptime(postData['form_release'], "%Y-%m-%d") > datetime.now():
                errors['no_future_release'] = "Cannot enter a future date for release date"
        except:
                errors['empty_release'] = "Release date required"

        if len(postData['form_desc']) > 1 and len(postData['form_desc']) < 10:
            errors['desc_length'] = "Description must be at least 10 characters"

        return errors
    def edit_show_validator(self, postData):
        errors = {}
        NameOfAllShows = Show.objects.filter(show_title=postData['new_title'])
        if len(postData['new_title']) < 2:
            errors["title_length"] = "Blog name should be at least 2 characters"
        elif len(postData['new_title']) > 45:
            errors["title_length"] = "Blog name should be less than 46 characters"
        if len(postData['new_network']) < 2:
            errors["network_length"] = "Blog name should be at least 2 characters"
        elif len(postData['new_network']) > 15:
            errors["network_length"] = "Blog name should be less than 16 characters"
            #convert date time from a string to a number
            # make sure release date is in the past
        try:    
            if datetime.strptime(postData['new_release'], "%Y-%m-%d") > datetime.now():
                errors['no_future_release'] = "Cannot enter a future date for release date"
        except:
                errors['empty_release'] = "Release date required"

        if len(postData['new_desc']) > 1 and len(postData['new_desc']) < 10:
            errors['desc_length'] = "Description must be at least 10 characters"

        return errors

class Show(models.Model):
    show_title = models.CharField(max_length=45)
    show_network = models.CharField(max_length=15)
    show_release = models.DateField()
    show_desc = models.CharField(max_length=1999)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

def __repr__(self):
    return (f"title: {self.show_title} ID: {self.id}")