from django import forms
from .models import statestic

class statesticform(forms.ModelForm):
    class Meta:
        model = statestic
        fields = '__all__'
        widgets = {
            'schools': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'мактаблар'}),
            'techers': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ўқтувчилар'}),
            'student': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ўқувчилар'}),
            'educati': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'м.т.м'}),
            'techedu': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'тарбиячилар'}),
            'chiledu': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'тарбияланувчилар'}),
        }
        labels = {
            'schools': 'мактаблар',
            'techers': 'ўқтувчилар',
            'student': 'ўқувчилар',
            'educati': 'м.т.м',
            'techedu': 'тарбиячилар',
            'chiledu': 'тарбияланувчилар',
        }

    # schools = models.CharField(max_length=200, blank=True, null=True)
    # techers = models.CharField(max_length=200, blank=True, null=True)
    # student = models.CharField(max_length=200, blank=True, null=True)
    # educati = models.CharField(max_length=200, blank=True, null=True)
    # techedu = models.CharField(max_length=200, blank=True, null=True)
    # chiledu = models.CharField(max_length=200, blank=True, null=True)