from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
from . models import Blog

class EditProfileForm(UserChangeForm):
    class Meta:
        User = get_user_model()
        model = User
        fields = ['first_name','last_name','bio','dp']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['user','views']
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.Textarea(attrs={'class':'form-control'})
           

        }