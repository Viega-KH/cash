from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class positionlevel(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class infolevel(models.Model):
    title = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    titletext = models.CharField(max_length=200, )
    number_ch =  models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    number_ep  =  models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class officelevel(models.Model):
    positiono = models.ForeignKey(positionlevel, on_delete=models.CASCADE)
    wslevel = models.ForeignKey(infolevel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last = models.CharField(max_length=100, )
    acceptance = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, )
    image = models.ImageField(upload_to='offis/')
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    

    
