from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name ='like_record',null = False)
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name ='like_record',null = False)

    class Meta: #장고에서만 적용하는 메타 클래스 이다  Db 에 적용할수 있는 조건
        unique_together = ['user','article'] # 한 유저가 한개의 게시글에 좋아요만 누르기 때문에 유니크 한 설정을 적용해야 한다.