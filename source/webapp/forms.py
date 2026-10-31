from django import forms
from django.forms import widgets

class GuestForm(forms.Form):
    author_name = forms.CharField(max_length=100,required=True, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    author_email = forms.EmailField(max_length=100,required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), required=True, label='Текст')

class DeleteForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='Введите email автора записи для подтверждения',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )