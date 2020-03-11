from django.db import models

# Create your models here.
# Book/Authors (shell)Start
class books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "title: {}".format(self.title)
    
class authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(books, related_name="Authors")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "id: {} last name: {}".format(self.id, self.last_name)
        

# Book/Authors (shell)End