from django.db import models
import uuid

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'

    def __str__(self):
        return self.title


