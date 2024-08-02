from django.db import models

# Create your models here.
class contactlink(models.Model):
    location = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    telegram = models.URLField(max_length=200, null=True)
    twitter = models.URLField(max_length=200, null=True)
    instagram = models.URLField(max_length=200, null=True)
    facebook = models.URLField(max_length=200, null=True)
    call = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f'{self.location} - {self.email}'
