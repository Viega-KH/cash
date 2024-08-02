# serializers school
from rest_framework import serializers
from school.models import positionschool, infoschool, officeschool
from slevel.models import positionlevel, infolevel, officelevel

class positionserializersch(serializers.ModelSerializer):
    class Meta:
        model = positionschool
        fields = [ 'title' ]

class infoserializersch(serializers.ModelSerializer):
    class Meta:
        model = infoschool
        fields = '__all__'

class officeserializersch(serializers.ModelSerializer):
    positiono = positionserializersch()
    class Meta:
        model = officeschool
        fields = '__all__'


# serializers slevel
        
class infoserializersle(serializers.ModelSerializer):
    class Meta:
        model = infolevel
        fields = '__all__'

class positionserializersle(serializers.ModelSerializer):
    class Meta:
        model = positionlevel
        fields = '__all__'

class officeserializersle(serializers.ModelSerializer):
    positiono = positionserializersle()
    class Meta:
        model = officelevel
        fields = '__all__'