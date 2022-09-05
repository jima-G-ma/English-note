from .models import Book, Post
from django import forms

class WordForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs["class"] = "form-control"
    self.fields['book'].widget.attrs['readonly'] = 'readonly'

  class Meta:
    model = Post
    fields = ('book', 'question', 'answer', 'category',)
    labels =  {'book': '単語帳', 'question': '問題', 'answer': '答え', 'category': 'カテゴリー'}
  
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('book', 'question', 'answer', 'category',)
    labels =  {'book': '単語帳', 'question': '問題', 'answer': '答え', 'category': 'カテゴリー'}

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ('name',)
    labels = {'name': '名前'}
