from django.forms import ModelForm
from custom_accounts.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _




# class MyUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['name', 'username', 'email', 'password1', 'password2']


class MyUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'class': 'form-control',
            'placeholder': 'Email',
        })
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'id': 'username',
            'class': 'form-control',
            'placeholder': 'Username',
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'id': 'password1',
            'class': 'form-control',
            'placeholder': 'Password',
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'id': 'password2',
            'class': 'form-control',
            'placeholder': 'Confirm Password',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'phone']  # Adjust the fields as needed

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_('Email'), max_length=250, widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class ChangePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'id': 'new_password1',
            'class': 'form-control',
            'placeholder': 'New Password',
        })
    )
    new_password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'id': 'new_password2',
            'class': 'form-control',
            'placeholder': 'Confirm New Password',
        })
    )
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']