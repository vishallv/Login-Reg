from __future__ import unicode_literals
from django.db import models


import re

class UserManager(models.Manager):
    def basic_validation(self,postData):
        error = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name'])<2:
            error["first_name"]="Enter more than character 2 for first name"
            
        if len(postData['last_name'])<2:
            error["last_name"]="Enter more than character 2 for last name"
        
        if postData['pass'] != postData['cpass']:
            error["password"]="Password does not match"
            
        if not EMAIL_REGEX.match(postData['email']): 
            error["email"]="Enter a valid Email"
            
        return error


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    hexVal = models.CharField(max_length=15,null=True)
    objects = UserManager()
    
