from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from articleapp.decorator import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    #success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'articleapp/create.html'

    def form_valid(self, form): #검증이 끝나면 마지막에 실행되는 메소드
        form.instance.writer = self.request.user #글이 작성 되면 요청을 보내는 유저의 정보를 보낸다
        return super().form_valid(form)
    def get_success_url(self): #detail page 가 생겼으므로 수정하고 나서 해당 pk 로 등록된 게시글로 가는 방법
        return reverse('articleapp:detail',kwargs={'pk':self.object.pk})

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article' #접근 하기 위한 패턴
    template_name = 'articleapp/detail.html'

@method_decorator(article_ownership_required,'get')
@method_decorator(article_ownership_required,'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    #success_url = reverse_lazy('articleapp:detail')
    template_name = 'articleapp/update.html'

    def get_success_url(self): #detail page 가 생겼으므로 수정하고 나서 해당 pk 로 등록된 게시글로 가는 방법
        return reverse('articleapp:detail',kwargs={'pk':self.object.pk})



@method_decorator(article_ownership_required,'get')
@method_decorator(article_ownership_required,'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 1 #20개의 object 가 들어간다