from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@transaction.atomic  # atomic 을 적용하면 db transaction 에서 like 를 추가하는 과정부터 좋아요 가 올라가는것 까지 한꺼번에 작용한다.
def db_transaction(user, article):


    likeRecord = LikeRecord.objects.filter(user=user, article=article)

    if likeRecord.exists():  # 게시글에 좋아요 했던 기록이 있으면 그페이지 로 돌아간다
        raise ValidationError("like already exists")

    else:
        LikeRecord(user=user, article=article).save()
        article.like += 1  # 좋아요 1 증가 를 시키고
        article.save()


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])

        try:
            db_transaction(user, article)
            # 좋아요 가 정상 실행
            '''
            likeRecord.delete()
            article.like -= 1
            article.save()
            '''
            messages.add_message(request, messages.SUCCESS, "좋아요가 반영되었습니다")
        except ValidationError:
            # 좋아요 반영 되지 않은 메세지
            messages.add_message(request, messages.ERROR, "좋아요는 한번만 가능합니다")
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']}))
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']})
