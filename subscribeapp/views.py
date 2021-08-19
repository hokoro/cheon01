from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

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