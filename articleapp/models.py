from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='article',null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True) #게시글과 연결고리 역으로 추적하는 방식이다
    #글쓴 사람이 한개 가 아닌 더많은 게시글을 작성해야 되서
    #SET_NULL = 작성자 미상 SET NULL
    #user.article 유저 객체 가 게시글 접근 하기 위해서 related_name = 'article' 로 설정

    title = models.CharField(max_length=200,null=True)

    image = models.ImageField(upload_to='article/',null = True)
    #upload_to 올리기 전에는 media folder 가 없고 웹을 실행 하면 image 들이  media 폴더 안에 article 폴더로 생성 되어 저장된다

    content = models.TextField(null = True) #장문의 글을 받을수 있도록 설정하는 것

    created_at = models.DateField(auto_now_add= True,null=True) #언제 글을 작성 했는지 정보를 받아온다. 서버 나 클라이언트 에 설정 을 받아오는게 아니라 생성 되면 바로 저장