from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'
    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.article.pk}) #원하는 해당 게시글로 보낸다.
        #할당을 안해줬다..? = 게시글 작성자랑 게시글을 아직 못받아서 데이터가 없다 db 에도 현재 null 로 초기화
    def form_valid(self, form):
        form.instance.writer = self.request.user #로그인 하고 해야함
        form.instance.article_id = self.request.POST.get('article_pk') #POST 형식 안에 저장된 article_pk 를 받아서 게시글 id 로 설정해주는거다
        return super().form_valid(form)
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.article.pk}) #삭제 하고나서 연결되있던 게시글로 넘어간다
