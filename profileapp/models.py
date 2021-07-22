from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    #accountapp 과 1ㄷ1 매칭
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile') #profile 과 user 를 연결
    '''
    계정이 삭제시 profile 에 대한 행위 on_delete = models.CASCADE 
    계정이 삭제되면 프로필도 종속되어 삭제 된다.
    SET_NULL  =  NULL 로 설정한다
    related_name 1ㄷ1 연결시 user 에서 profile 을 불러올떄 user.profile 간단하게 연결고리 매개변수 
    '''
    #image 처리
    image = models.ImageField(upload_to='profile/',null = True)
    '''
    upload_to : 어디로 업로드 할건지에 대한 내용 위치 를 나타내는 매개변수 
    null = True : 공백으로 놔두어도 되는지 (사진이 없어도 프로필 만들수 있다 , 비어있어도 무방하다)
    '''
    #nickname
    nickname = models.CharField(max_length=30,unique=True,null = True)
    '''
    maxlength 최대 길이
    unique : 중복 허용 금지
    null : text 가 없어도 상관 없는지 여부 
    '''
    #message
    message = models.CharField(max_length=200,null = True)
    '''
    maxlength 최대 길이
    null : text 가 없어도 상관 없는지 여부 
    '''


