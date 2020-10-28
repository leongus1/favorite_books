from django.db import models
from login_app.models import Users

# Create your models here.
class BookManager(models.Manager):
    def book_validator(self, postData):
        errors={}
        if not len(postData['title'])>0:
            errors['title'] = "Title is required"
        if len(postData['description'])<5:
            errors['description'] = "Description must be at least 5 characters"
        return errors

class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(Users, related_name="books_uploaded",on_delete=models.CASCADE)    
    users_who_like = models.ManyToManyField(Users, related_name="liked_books")
    objects = BookManager()
    
