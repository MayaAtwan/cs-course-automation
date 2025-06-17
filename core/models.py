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
    GROUP_CHOICES = [
        ('individual', 'Individual'),
        ('pair', 'Pair'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    group_type = models.CharField(max_length=10, choices=GROUP_CHOICES)
    exercises = models.ManyToManyField(Exercise)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
