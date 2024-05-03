from .models import ContactUs
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['sender_firstname', 'sender_lastname', 'sender_email', 'message']

        widgets = {
            'sender_firstname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Firstname'
            }),
            'sender_lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lastname'
            }),
            'sender_email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '4',
                'placeholder': 'Write your message...'
            }),
        }


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'field_class form-control',
        'placeholder': 'Create Strong Password'
    }))
    password2 = forms.CharField(label='Conformation Password', widget=forms.PasswordInput(attrs={
        'class': 'field_class form-control',
        'placeholder': 'Confirm Your Password'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'field_class form-control',
                'placeholder': 'Create Strong Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'field_class form-control',
                'placeholder': 'Enter your Firstname',
                'required': True,
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'field_class form-control',
                'placeholder': 'Enter your Lastname',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'field_class form-control',
                'placeholder': 'Enter your Email Address',
                'required': True,
            })
        }


class SignInForm(AuthenticationForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'field_class form-control',
        'placeholder': 'Enter Your Password'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'field_class form-control',
        'placeholder': 'Enter Your Username'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']

