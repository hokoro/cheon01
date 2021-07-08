from django.db import models

# Create your models here.

class HelloWorld(models.Model): #models 에 있는 Model 을 상속 받는다.
    text = models.CharField(max_length=255,null = False) #문자열 필드를 받아 TEXT 를 받는 CHARFIELD 를 생성
    '''
    max_length = 최대 길이 
    null = True/Fasle 텍스트의 데이터가 비어있어도 되는지 설정 하는것이다.
    변화를 추적해야 한다. 모델은
    '''

