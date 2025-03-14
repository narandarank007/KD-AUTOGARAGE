from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from lapp.models import Booking
from django import forms


class UserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Enables a calendar picker

    class Meta: 
     
        model = Booking
        fields = ['email','phone','CarBrand','ModelName','address', 'date','pickup_slot','service_category']
              