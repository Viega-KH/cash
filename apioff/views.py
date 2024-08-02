# views.py
from rest_framework import generics
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from school.models import positionschool, infoschool, officeschool
from slevel.models import positionlevel, infolevel, officelevel
from .serializers import (
    positionserializersch, infoserializersch, officeserializersch,
    positionserializersle, infoserializersle, officeserializersle
)

# School views

class officeschoolfilter(django_filters.FilterSet):
    wschool_id = django_filters.NumberFilter(field_name='wschool__id', lookup_expr='exact')

    class Meta:
        model = officeschool
        fields = ['wschool_id']


class positionschoollist(generics.ListCreateAPIView):
    queryset = positionschool.objects.all()
    serializer_class = positionserializersch

class infoschoollist(generics.ListCreateAPIView):
    queryset = infoschool.objects.all()
    serializer_class = infoserializersch
class infoschooldetail(generics.RetrieveAPIView):
    queryset = infoschool.objects.all()
    serializer_class = infoserializersch

class officeschoollist(generics.ListCreateAPIView):
    queryset = officeschool.objects.all()
    serializer_class = officeserializersch
    filter_backends = (DjangoFilterBackend,)
    filterset_class = officeschoolfilter

# Slevel views
class officeslevelfilter(django_filters.FilterSet):
    wschool_id = django_filters.NumberFilter(field_name='wslevel__id', lookup_expr='exact')

    class Meta:
        model = officelevel
        fields = ['wslevel_id']   

class positionlevellist(generics.ListCreateAPIView):
    queryset = positionlevel.objects.all()
    serializer_class = positionserializersle

class infolevellist(generics.ListCreateAPIView):
    queryset = infolevel.objects.all()
    serializer_class = infoserializersle

class infoleveldetail(generics.RetrieveAPIView):
    queryset = infolevel.objects.all()
    serializer_class = infoserializersle

class officelevellist(generics.ListCreateAPIView):
    queryset = officelevel.objects.all()
    serializer_class = officeserializersle
    filter_backends = (DjangoFilterBackend,)
    filterset_class = officeslevelfilter
