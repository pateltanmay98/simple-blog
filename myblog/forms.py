from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Tag'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Post Body'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Tag'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Post Body'}),
        }