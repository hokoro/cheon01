from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

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
        '''
        form = profilecreationsform 인데 forms.py 에는 user 에 대한 정보 가 없다 
        따라서 instance: form 이 생성 될때 만들어진 user 를 request 요청한 user 에 넣어준다.
        '''
        return super().form_valid(form) #검증하는 모든 과정이 실행 되고 나서 이후에 실행 되는 함수 + 우리는 user 만 커스터 마이징 함

class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile' #업데이트 할 프로필 지정
    form_class = ProfileCreationsForm
    success_url =  reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'