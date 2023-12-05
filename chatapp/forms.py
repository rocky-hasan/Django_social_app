# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.Form):
    text = forms.CharField(label='Comment', widget=forms.TextInput(attrs={'rows': 5,'name':'text'}))
    class Meta:
        model = Comment
        fields = ['text']
    
