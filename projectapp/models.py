from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20,null=False) #제목은 꼭 필요함
    description = models.CharField(max_length=200,null = True,blank=True) #설명문 없어도 괜춘함 데이터 베이스 내의 null 여부 , blank 는 html 에서 입력 여부
    image = models.ImageField(upload_to='project/',null = False)
    created_at = models.DateTimeField(auto_now_add=True) #자동으로 날짜 생성
