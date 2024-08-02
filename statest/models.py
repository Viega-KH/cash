from django.db import models

# Create your models here.
class statestic(models.Model):
    schools = models.CharField(max_length=200)
    techers = models.CharField(max_length=200)
    student = models.CharField(max_length=200)
    educati = models.CharField(max_length=200)
    techedu = models.CharField(max_length=200)
    chiledu = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.schools}-{self.educati}'