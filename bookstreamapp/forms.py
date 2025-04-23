from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BookTable
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = ['btitle', 'blogo', 'bauthor', 'bgenre', 'bdescription']
        
        labels = {
            'btitle' :'Title',
            'blogo': 'Book Logo',
            'bauthor'    :'Author',
            'bgenre':'Genre',
            'bdescription':'Description',
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

