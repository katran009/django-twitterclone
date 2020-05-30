from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    display_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    

