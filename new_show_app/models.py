from django.db import models

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Provided TITLE needs to be at least 2 characters"
        if len(postData['network']) < 5:
            errors["network"] = "Provided NETWORK needs to be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Provided DESCRIPTION needs to be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=150)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() #override the objects = models.Manager()
    

# Create your models here.
