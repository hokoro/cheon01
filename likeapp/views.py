from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required,'get')
class LikeArticleView(RedirectView):
    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk = kwargs['article_pk'])

        likeRecord = LikeRecord.objects.filter(user= user ,article = article) #좋아요 정보 를 filter

        if likeRecord.exists(): #게시글에 좋아요 했던 기록이 있으면 그페이지 로 돌아간다
            '''
            likeRecord.delete()
            article.like -= 1
            article.save()
            '''
            return HttpResponseRedirect(reverse('articleapp:detail',kwargs={'pk':kwargs['article_pk']}))
        else:
            LikeRecord(user=user , article=article).save()
            article.like +=1 #좋아요 1 증가 를 시키고
            article.save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail',kwargs={'pk':kwargs['article_pk']})