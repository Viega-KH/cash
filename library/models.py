from django.db import models


class librarycategore(models.Model):
    name = models.CharField(max_length=225)
    def __str__(self):
        self.name

class library(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='library/')
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        self.name