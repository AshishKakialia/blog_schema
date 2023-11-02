from django import forms
from .models import *
from django.contrib.auth.password_validation import validate_password


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}),validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm_password'}),validators=[validate_password])
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    # email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email'}))
   
    class Meta:
        model = ExtendUser
        fields = ['username', 'password', 'confirm_password']

    # Password match validator function
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                return forms.ValidationError(
                    'password and confirm_password does not match'
                )
        return cleaned_data
