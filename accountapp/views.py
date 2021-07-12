from django.http import HttpResponse, HttpResponseRedirect  # HttpResponse 메소드를 사용할려는 라이브러리
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    #POST/GET 방식에 대한 분기 문 을 작성
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

    #HttpResponse('Hello World')

'''
app 안에 template 만들고 accountapp 폴더를 따로 만드는 이유 
파일만 남겨두면 어디서 가져오는 파일인지 알수가 없다 
왜냐 하나의 프로젝트에는 여러가지의 앱이 들어가기 때문에 파일에 경로 로 만들어야 어디앱 에 어떤 파일인지 구분할수 있기 때문이다.
'''