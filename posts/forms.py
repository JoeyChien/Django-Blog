from django import forms
from django.utils.translation import gettext_lazy as _ 
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'title'   : _('標題'),
            'content' : _('內容'),
            'category': _('分類'),
        }
