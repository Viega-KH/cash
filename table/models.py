from django.db import models
from school.models import infoschool
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


    
class wclases(models.Model):
    title = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(11)])
    published_date = models.DateField(auto_now_add=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.title}'
    

class lesson(models.Model):
    wschool = models.ForeignKey(infoschool, on_delete=models.CASCADE)
    wclass = models.ForeignKey(wclases, on_delete=models.CASCADE)
    file = models.FileField(upload_to='lesson/')
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.wschool)