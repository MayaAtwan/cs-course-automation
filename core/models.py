from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    title      = models.CharField(max_length=255)
    content    = models.TextField()
    difficulty = models.CharField(max_length=50, blank=True)
    # פשוט נשתמש בטקסט שיאכסן את התגיות
    tags = models.JSONField(blank=True, null=True)


    def __str__(self):
        return self.title

class Assignment(models.Model):
    name     = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True, blank=True)
    author   = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
