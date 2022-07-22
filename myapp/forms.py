from django import forms
from .models import Blog, Comment, HashTag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'image', 'hashtags']
        
class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ['text']
        
class HashTagForm(forms.ModelForm) :
    class Meta :
        model = HashTag
        fields = ['name']