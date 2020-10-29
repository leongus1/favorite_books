from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def user_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postData['first_name'])<2:
            errors['first_name'] = "First name should be at least 2 characters long."
        if len(postData['last_name'])<2:
            errors['last_name'] = "Last name should be at least 2 characters long."
        if len(postData['password'])<8:
            errors['password_len'] = "Password should be at least 8 characters long."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_format'] = "Email format is invalid."
        if not postData['password']==postData['conf_pw']:
            errors['pw_match'] = "Passwords do not match."
            
        return errors
        
            


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
