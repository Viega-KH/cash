from django.contrib import admin
from .models import infoschool, officeschool, positionschool
# Register your models here.

admin.site.register([ infoschool, officeschool, positionschool ])
