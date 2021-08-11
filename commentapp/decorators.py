from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request,*args,**kwargs):
        #request 를 보내는 유저 comment 의 writer 를 확인 해야 한다
        target_comment = Comment.objects.get(pk=kwargs['pk'])
        if target_comment.writer == request.user:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseForbidden()
    return decorated