from django.urls import path
from django.views.generic import TemplateView

app_name = 'articleapp'
urlpatterns = [
    path('list/',TemplateView.as_view(template_name='articleapp/list.html'),name = 'list') #템플릿만 가져와서 보여주는 템플릿 뷰를 사용
]
