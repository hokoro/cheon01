from django.contrib import admin
from django.urls import path,include

from accountapp.views import hello_world #함수 가져오기

app_name = 'accountapp'
urlpatterns = [
    path('hello_world/',hello_world,name= 'hello_world'),
    #path('url에 입력할 주고',사용할 함수 가져오기 ,name = 사용할 이름)
]