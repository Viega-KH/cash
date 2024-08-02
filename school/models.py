from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class positionschool(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

class infoschool(models.Model):
    title = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    titletext = models.CharField(max_length=200)
    number_pt = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    number_s = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class officeschool(models.Model):
    positiono = models.ForeignKey(positionschool, on_delete=models.CASCADE)
    wschool = models.ForeignKey(infoschool, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    acceptance = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    image = models.ImageField(upload_to='offis/')
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
    
    

    
