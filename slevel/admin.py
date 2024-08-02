from django.contrib import admin
from .models import infolevel, officelevel, positionlevel
# Register your models here.


admin.site.register([ infolevel, officelevel, positionlevel ])