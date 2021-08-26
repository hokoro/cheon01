from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'min-height:10rem;'
                                                                    'text-align: left;'}))  # forms 안에 charfield 를 사용하여 class customizing 을 한다  textarea 라는 widget 을 사용한다.

    class Meta:  # 외부 정보를 얻기 위해서 받는 meta class
        model = Article
        fields = ['title', 'project', 'image', 'content']
