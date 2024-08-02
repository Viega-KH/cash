from django.contrib import admin
from .models import librarycategore, library
# Register your models here.

admin.site.register([librarycategore, library])