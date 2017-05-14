from django import forms
from GeoRiddles.models import User, Mystery

users = User.objects.all()

class AddMysteryForm(forms.Form):
    name = forms.CharField(max_length=64)
    gc_code = forms.CharField(max_length=16)
    description = forms.CharField()
    location = forms.CharField(max_length = 64)
    latitude = forms.DecimalField(label = 'N',max_digits = 8, decimal_places = 6, initial = '52.330204', required = True)
    longitude = forms.DecimalField(label = 'E',max_digits = 8, decimal_places = 6, initial = '19.974818', required = True)
    added_by = forms.CharField(label='Dodane przez',widget=forms.TextInput(attrs={'readonly':'readonly'}))