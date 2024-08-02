from django.db import models
from school.models import infoschool
# Create your models here.
class club(models.Model):
    wschool = models.ForeignKey(infoschool, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    leader = models.CharField(max_length=255)
    days = models.CharField(max_length=255)
    meeting_time = models.CharField(max_length=255)
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name