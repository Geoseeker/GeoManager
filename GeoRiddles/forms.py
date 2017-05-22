from django import forms
from django.contrib.gis import forms
from GeoRiddles.models import User, Mystery
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.auth import authenticate


users = User.objects.all()

class AddMysteryForm(forms.Form):
    name = forms.CharField(max_length=64)
    gccode = forms.CharField(max_length=16)
    description = forms.CharField()
    location = forms.CharField(widget=GooglePointFieldWidget)
    foto = forms.ImageField(label='dodaj zdjęcie')
#     latitude = forms.DecimalField(label = 'N',max_digits = 8, decimal_places = 6, initial = '52.330204', required = True)
#     longitude = forms.DecimalField(label = 'E',max_digits = 8, decimal_places = 6, initial = '19.974818', required = True)
    added_by = forms.CharField(label='Dodane przez',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
class MyGeoForm(forms.Form):
    point = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
       
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data['username']
        password = cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Błędny login lub hasło')
        cleaned_data['user'] = user        
        return cleaned_data