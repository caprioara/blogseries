from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm # (rescrie unele parti din code ale lui django)
from django.core.exceptions import ValidationError

# forms - https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/

class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        test = User.objects.filter(email=email)
        if not test:
            raise forms.ValidationError('Unfortunetley we can not find that email address')
        return email


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError('Username already exists')
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'E-mail': 'name'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'}
        )