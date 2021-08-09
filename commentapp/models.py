from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    # 1:many 연결  set null 지우지는 않고 연결되는 게시글이 null 로 초기화 됨 related name : 연결된 이름
    article = models.ForeignKey(Article,on_delete = models.SET_NULL,related_name='comment',null = True)
    writer = models.ForeignKey(User,on_delete= models.SET_NULL,related_name='comment',null = True)

    #forms 에서는 여기만 사용함
    content = models.TextField(null = False)

    created_at = models.DateTimeField(auto_now_add=True) #DB 에 저장되면 바로 날짜 가 기록
