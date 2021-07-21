from django.contrib.auth.forms import UserCreationForm #유저가 생성할떄 필요한 form
from django.contrib.auth.models import User #기본적으로 생성시 필요한 유저 모델
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden  # HttpResponse 메소드를 사용할려는 라이브러리
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, \
    DeleteView  # 장고 -> view -> generic -> createview 를 가져옴

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


def hello_world(request):
    if request.user.is_authenticated: #계정이 로그인 됬는지 확인
    #POST/GET 방식에 대한 분기 문 을 작성 +로그인 할떄만 정보 처리를 할수 있게 만들기
        if request.method == 'POST':
            temp = request.POST.get('input') #input 으로 입력 한 데이터 를 post.get 을 사용해 얻어 온다
    
            new_data = HelloWorld()
            new_data.text = temp  #client 로 받아온 data 를 db 모델에 저장한다.
            new_data.save() #client 로 받은 데이터를 실제 db 에 저장
            '''
            data_list = HelloWorld.objects.all() #helloworld 모델의 객체들을 가져온다 all = 모든정보를 빼온다.
            return render(request,'accountapp/hello_world.html',context={'data_list': data_list}) #html 파일을 가져오고 싶을떄 context
            #객체를 실제 context text 에 적용
            '''
            #redirect 적용
            return HttpResponseRedirect(reverse('accountapp:hello_world'))
            #역으로 추적해주는  'accountapp:hello_world' 이렇게 작성 하면 'accountsapp/hello_world hello_world -> accountsapp 으로 역추적을 해준다
            #간편하게 사용하기 위해
            #'appname : templates 파일'
            #어디로 재연결 할지 내용을 적는다. + 어떤 app 에 어떤 라우트 로 가라고 알려줌
    
        else:
            data_list = HelloWorld.objects.all()
            return render(request,'accountapp/hello_world.html',context={'data_list':data_list})
            #get 방식으로 해도 모든 리스트 들이 db 에서 가져 올수 있다.
    
    else:
        return HttpResponseRedirect(reverse('accountapp:login')) #로그인 이 안돼있으니까 로그인 하라는 주소로 재연결 시킨다.
    #HttpResponse('Hello World')

'''
app 안에 template 만들고 accountapp 폴더를 따로 만드는 이유 
파일만 남겨두면 어디서 가져오는 파일인지 알수가 없다 
왜냐 하나의 프로젝트에는 여러가지의 앱이 들어가기 때문에 파일에 경로 로 만들어야 어디앱 에 어떤 파일인지 구분할수 있기 때문이다.
'''
#class based view
class AccountCreateView(CreateView): #Account 계정을 createview 로 만든다.
    model = User #user 생성
    #입력 형식 데이터
    form_class = UserCreationForm #user 형식 생성
    success_url = reverse_lazy('accountapp:hello_world') #접속시 연결하는 url
    # laze 를 쓰는 이유 : class 에서 값일 불러지는 방식이 함수랑 다르기 때문이다 나중에 값을 되돌려 줄수 있도록
    template_name = 'accountapp/create.html'
class AccountDetailView(DetailView): #장고에서 제공하는 CBV
    model = User #장고에서 서버 요청을 보내는 유저를 설정
    context_object_name = 'target_user' #server에서 찾아야 하는 타깃 유저 ,html 에서 뽑아낸 값을 접근할것인디
    template_name = 'accountapp/detail.html' #accountapp 에 있는 detail.html 에서 보여준다





class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm #업데이트 한 정보를 가져올 form class 가져오기 #id 를 제외한 나머지 form 보여주기
    context_object_name = 'target_user' #바뀐 정보에 접근 하기 위한 변수
    success_url = reverse_lazy('accountapp:hello_world') #데이터를 post 해준 hello world 로 연결
    template_name = 'accountapp/update.html' #보여줄 template_html 이름

    #class method 를 통한 회원 정보 접근
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated and self.get_object() == request.user: #로그인이 되있다면 get_object() = target object 를 찾는다 key 값을 가지고 있는
            return super().get(request,*args,**kwargs) #get 방식 핵심 알고리즘 인데
        else:
            return HttpResponseForbidden() #로그인 안되있다면 접근 금지 경고창 띄위기 :httpResponeforbidden()
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated and self.get_object() == request.user: #로그인이 되있다면
            return super().post(request,*args,**kwargs) #post 방식 핵심 알고리즘 인데
        else:
            return HttpResponseForbidden() #로그인 안되있다면 접근 금지 경고창 띄위기 :httpResponeforbidden()
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user' #접근할 유저
    success_url = reverse_lazy('accountapp:hello_world') #성공하면 연결할 url
    template_name = 'accountapp/delete.html' #보여질 template name

    # class method 를 통한 회원 정보 접근
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:  # 로그인이 되있다면 + key 값이 같은지 확인
            return super().get(request, *args, **kwargs)  # get 방식 핵심 알고리즘 인데
        else:
            return HttpResponseForbidden() #로그인 안되있다면 접근 금지 경고창 띄위기 :httpResponeforbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:  # 로그인이 되있다면
            return super().post(request, *args, **kwargs)  # post 방식 핵심 알고리즘 인데
        else:
            return HttpResponseForbidden() #로그인 안되있다면 접근 금지 경고창 띄위기 :httpResponeforbidden()