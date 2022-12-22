from django.db import models

# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    completed = models.BooleanField(default=False)

def __str__(self):
    return self.title