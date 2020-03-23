from django.db import models
from datetime import datetime
from django.utils import timezone
from datetime import timedelta
from loginApp.models import user

class Comment_Manager(models.Manager):
    def delete_comment_validator(self, postData):
        errors = {}
        Comment = Comments.objects.get(id=postData['delete_comment_id'])
        if (timezone.now() - Comment.created_at) > timedelta(minutes=30):
                errors['comment_max_30'] = "Comment deletable for only 30 minutes after creations"
        return errors

class Messages(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #1:many relationship to users
    user = models.ForeignKey(user, related_name="messages", on_delete = models.CASCADE)
    
class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #1:many relationship to messages
    messages = models.ForeignKey(Messages, related_name="comments", on_delete = models.CASCADE)
    #1:many relationship to users
    user = models.ForeignKey(user, related_name="comments", on_delete = models.CASCADE)
    objects = Comment_Manager()
