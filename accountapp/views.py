from django.http import HttpResponse #HttpResponse 메소드를 사용할려는 라이브러리 
from django.shortcuts import render


# Create your views here.
def hello_world(request):
    return render(request,'base.html') #html 파일을 가져오고 싶을떄
    #HttpResponse('Hello World')