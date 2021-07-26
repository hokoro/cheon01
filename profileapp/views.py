from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationsForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile #만들었던 model 가져오기
    form_class = ProfileCreationsForm #client 가 넣은 데이터 폼
    success_url = reverse_lazy('accountapp:hello_world') #연결 성공 하면 어디로 연결 account_app 으로 연결가능한것은 app_name 을 찾아서 이다.
    template_name = 'profileapp/create.html'

    #user_id 문제 해결  overideing
    def form_valid(self, form):
        #user 를 특정 해줘야 한다
        form.instance.user = self.request.user #client 에서 받아온 user == request 에서 받아온 유저
        return super().form_valid(form)

