from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from .models import RentedCar,Carrent


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    last_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    username = forms.CharField(max_length=254,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    password1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))
    password2=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class DateForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today,label='From:',required=False, widget= forms.TextInput(attrs={'class':'d-form form-control','placeholder':'YYYY-MM-DD'}))

    class Meta:
        model = RentedCar
        fields = ('user','date')

class RegisterCar(forms.Form):
    car_name = forms.CharField(max_length=250,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    car_color=forms.CharField(max_length=250,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    transmission_type=forms.CharField(max_length=250,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    fuel_type=forms.CharField(max_length=250,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    costperday = forms.IntegerField(max_value=10000,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    car_num = forms.CharField(max_length=20,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    car_image=forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = Carrent
        fields = ('car_name','car_color','transmission_type','fuel_type','costperday','car_num','car_image')
