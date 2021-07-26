from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationsForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile #만들었던 model 가져오기
    form_class = ProfileCreationsForm
    success_url = reverse_lazy('accountapp:hello_world') #연결 성공 하면 어디로 연결 account_app 으로 연결가능한것은 app_name 을 찾아서 이다.
    template_name = 'profileapp/create.html'

