from django.urls import path
from .views.module1_views import home, about, leader, new, newad, newdet, contactsite, homeselekt
from .views.module2_views import tablesite


urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('office/', leader, name='leader'),
    path('news/', new, name='news'),
    path('new/ad/', newad, name='newad'),
    path('new/<int:id>/', newdet, name='newdet'),
    path('table/', tablesite, name='tablesite'),
    path('contact/', contactsite, name='contactsite'),
    path('home/select/', homeselekt, name='homeselekt'),
]
