from django.http import HttpResponse #HttpResponse 메소드를 사용할려는 라이브러리 
from django.shortcuts import render


# Create your views here.
def hello_world(request):
    #POST/GET 방식에 대한 분기 문 을 작성
    if request.method == 'POST':
        return render(request,'accountapp/hello_world.html',context={'text':'POST METHOD'}) #html 파일을 가져오고 싶을떄 context
    else:
        return render(request,'accountapp/hello_world.html',context={'text':'GET'})


    #HttpResponse('Hello World')

'''
app 안에 template 만들고 accountapp 폴더를 따로 만드는 이유 
파일만 남겨두면 어디서 가져오는 파일인지 알수가 없다 
왜냐 하나의 프로젝트에는 여러가지의 앱이 들어가기 때문에 파일에 경로 로 만들어야 어디앱 에 어떤 파일인지 구분할수 있기 때문이다.
'''