from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path,include

from accountapp.views import  AccountCreateView, AccountDetailView, AccountUpdateView, \
    AccountDeleteView  # 함수 가져오기

app_name = 'accountapp' #라우팅 할때 연결되는 이름
urlpatterns = [
    #path('url에 입력할 주고',사용할 함수 가져오기 ,name = 사용할 이름)
    path('login/',LoginView.as_view(template_name = 'accountapp/login.html'),name = 'login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('create/',AccountCreateView.as_view(),name = 'create'),
    path('detail/<int:pk>',AccountDetailView.as_view(),name = 'detail'), #어떤 객체를 볼지에 대한 키를 받아와야 한다. 아니면 에러 발생
    path('update/<int:pk>',AccountUpdateView.as_view(),name = 'update'), #update 로 key 를 보내줘야 한다.
    path('delete/<int:pk>',AccountDeleteView.as_view(),name = 'delete')
    #클래스에서 함수 호출 클래스 이름.as_view()
    #<int:pk> key 에 대한 값을 int 형으로 받아온다. = 여기로 들어갈려면 pk 의 값 이 무조건 필요 하다
]