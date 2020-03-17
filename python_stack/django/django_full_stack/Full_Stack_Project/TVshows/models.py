from django.db import models

class Show(models.Model):
    show_title = models.CharField(max_length=45)
    show_network = models.CharField(max_length=15)
    show_release = models.DateField()
    show_desc = models.CharField(max_length=1999)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

def __repr__(self):
    return (f"title: {self.show_title} ID: {self.id}")