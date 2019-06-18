from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control", 
                "placeholder":"FullName"
                }
                )
        )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Your Email"
                }
                )
        )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Message'
                }
                )
        )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("only gmail.com is allowed.")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Username',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Password',
            }
        )
    )
    
class RegisterForm(forms.Form):
    username = forms.CharField()
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label='Conform Password', widget=forms.PasswordInput())
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is taken.')
        
        return username
        

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Passwords must match')
        elif len(password) < 6:
            raise forms.ValidationError('Minimum length of Password is 6')

        return data

