#-*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea, TextInput
from models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
        widgets = {
            'comments_text':Textarea(attrs={'cols':80, 'rows':20}),
        }
        labels = {
            'comments_text':'Комментаридің мәтіні'
        }
