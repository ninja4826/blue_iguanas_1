from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

TASK_PRIORITY_CHOICES = (
    (0, 'low'),
    (1, 'moderate'),
    (2, 'high')
)

class Task(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    priority = models.IntegerField(choices=TASK_PRIORITY_CHOICES)
    
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created',)