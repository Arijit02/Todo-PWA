from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Todo
from django.contrib.auth.models import User


class TodoForm(forms.ModelForm):
    title = forms.CharField(max_length=20)
    item = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Todo
        fields = ["title", "item"]


'''
class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField()
    password = forms.CharField(
        max_length=20, required=True, widget=forms.PasswordInput)
    repeat_password = forms.CharField(
        max_length=20, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeat_password']
'''


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
