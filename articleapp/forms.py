from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta: #외부 정보를 얻기 위해서 받는 meta class
        model = Article
        fields = ['title','image','content']
