from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm #유저가 생성할떄 필요한 form
from django.contrib.auth.models import User #기본적으로 생성시 필요한 유저 모델
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden  # HttpResponse 메소드를 사용할려는 라이브러리
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, \
    DeleteView  # 장고 -> view -> generic -> createview 를 가져옴
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld
from articleapp.models import Article


@login_required(login_url= reverse_lazy('accountapp:login'))
def hello_world(request):
    #계정이 로그인 됬는지 확인
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
    
     #로그인 이 안돼있으니까 로그인 하라는 주소로 재연결 시킨다.
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
    #success_url = reverse_lazy('accountapp:hello_world') #접속시 연결하는 url
    # laze 를 쓰는 이유 : class 에서 값일 불러지는 방식이 함수랑 다르기 때문이다 나중에 값을 되돌려 줄수 있도록
    template_name = 'accountapp/create.html'

    def get_success_url(self):  # 계정이 연결되 있는 url 을 가져오기
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk}) #여기서는 바로 targetuser 이기 때문에 바로 pk 를 받는다
class AccountDetailView(DetailView,MultipleObjectMixin): #장고에서 제공하는 CBV
    model = User #장고에서 서버 요청을 보내는 유저를 설정
    context_object_name = 'target_user' #server에서 찾아야 하는 타깃 유저 ,html 에서 뽑아낸 값을 접근할것인디
    template_name = 'accountapp/detail.html' #accountapp 에 있는 detail.html 에서 보여준다

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object) #이 페이지 주인이 작성한 게시글만 보여준다
        return super().get_context_data(object_list = article_list,**kwargs)


has_ownership = [login_required,account_ownership_required]

@method_decorator(has_ownership,'get') #메소드에서 데코레이터를 적용한다 (적용할 데토레이터를 가져와야 한다,어떤 방식의 메소드 를 접근 할지)
@method_decorator(has_ownership,'post') #애초에 클래스 메소드에서 데코레이터를 작동할수 있는 시스템을 만들어야 한다.

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm #업데이트 한 정보를 가져올 form class 가져오기 #id 를 제외한 나머지 form 보여주기
    context_object_name = 'target_user' #바뀐 정보에 접근 하기 위한 변수
    #success_url = reverse_lazy('accountapp:hello_world') #데이터를 post 해준 hello world 로 연결
    template_name = 'accountapp/update.html' #보여줄 template_html 이름

    def get_success_url(self):  # 계정이 연결되 있는 url 을 가져오기
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk}) #여기서는 바로 targetuser 이기 때문에 바로 pk 를 받는다

#class method 를 통한 회원 정보 접근

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user' #접근할 유저
    success_url = reverse_lazy('accountapp:hello_world') #성공하면 연결할 url
    template_name = 'accountapp/delete.html' #보여질 template name

