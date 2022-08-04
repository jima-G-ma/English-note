from .models import Post
from django import forms

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('question', 'answer', 'category',)
    labels =  {'question': '問題', 'answer': '答え', 'category': 'カテゴリー'}