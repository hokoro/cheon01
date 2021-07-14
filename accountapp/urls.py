from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path,include

from accountapp.views import hello_world, AccountCreateView  # 함수 가져오기

app_name = 'accountapp' #라우팅 할때 연결되는 이름
urlpatterns = [
    path('hello_world/',hello_world,name= 'hello_world'),
    #path('url에 입력할 주고',사용할 함수 가져오기 ,name = 사용할 이름)
    path('login/',LoginView.as_view(template_name = 'accountapp/login.html'),name = 'login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('create/',AccountCreateView.as_view(),name = 'create'),
    #클래스에서 함수 호출 클래스 이름.as_view()

]