from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model): #구독정보만 필요하기 때문에 form 은 필요가 없다
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='subscription',null = False) #유저가 탈퇴하면 구독정보도 같이 삭제 한다

    project =models.ForeignKey(Project,on_delete=models.CASCADE,related_name='subscription',null=False) #게시판이 삭제되면 구독 정보도 삭제

    class Meta:
        unique_together = ['user','project'] #유저와 프로젝트는 한개의 쌍으로 한개만 존재하게 설정 한다