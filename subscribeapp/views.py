from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required,'get')
class SubscriptionView(RedirectView):
    def get(self, request, *args, **kwargs): #http protocol get
        user = request.user
        project = Project.objects.get(pk = kwargs['project_pk']) #주소창에 있는 project pk 받기

        subscription = Subscription.objects.filter(user = user,project = project) #찾아논 유저랑 게시판 을 동시에 만족하는 구독자를 찾는것이다


        #구독이 되어있으면 구독 취소
        if subscription.exists():
            subscription.delete()
        else:
            #구독이 안되있으면 구독 객체를 생성하여 저장 (save)
            Subscription(user=user,project=project).save()
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail',kwargs={'pk': kwargs['project_pk']})

@method_decorator(login_required,'get')
class SubscriptionListView(ListView):
    #게시글
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    #get context data 는 templates 의 모든 데이터를 조종 가능 할수 있다
    # 어떤 게시글을 볼건지 queryset 어떤 게시글 을 볼건지만 지정할수 있음 요소 하나만 사용
    def get_queryset(self):
        # 지금 접속한 유저의 모든 구독 정보를 가져온다 + 구독 모델에 안에 있는 project 만 가져옴 = values_list method
        project_list = Subscription.objects.filter(user = self.request.user).values_list('project')
        #그 프로젝트 안에 있는 게시글만 filter 를 시킨다.
        article_list = Article.objects.filter(project__in=project_list)

        return article_list