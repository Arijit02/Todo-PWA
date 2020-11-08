from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=20)
    item = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
