from django.forms import ModelForm
from .models import *
from django import forms
from django.db import models
# Создаём модельную форму


class PostAddForm(ModelForm):
    # author = forms.CharField(initial='value?', widget=forms.TextInput(
    #     attrs={'class': 'form-control', },),)

    # def __init__(self, *args, **kwargs):
    #     super(PostAddForm, self).__init__(*args, **kwargs)
    # self.fields['author'].disabled = True
    # self.fields['author'].queryset = queryset?
    # self.fields['author'].initial = 'value?

   #  def __init__(self, *args, **kwargs):
   #      super(PostAddForm, self).__init__(*args, **kwargs)
   #      uneditable_fields = ['author', 'title']
   #      for field in uneditable_fields:
   #          self.fields[field].widget.attrs['readonly'] = 'true'

    class Meta:
        model = Post
        fields = ['title', 'postType',
                  'postCategory', 'text', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название публикации'}),
            'postType': forms.Select(attrs={'class': 'form-control', }),
            'postCategory': forms.Select(attrs={'class': 'form-control', }),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст'}),
            'image': forms.FileInput(attrs={'class': 'form-control', }),

        }

        labels = {
            'title': 'Название',
            'postType': 'Класс',
            'postCategory': 'Категория',
            'text': 'Описание',
            'image': 'Фото/Картинка',
        }


class ResponseAddForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['text']
        widgets = {

            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст'}),

        }
