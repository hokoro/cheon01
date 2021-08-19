from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin #여러개의 오브젝트를 가져올수 있는

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    #success_url = reverse_lazy('articleapp:list')
    template_name = 'projectapp/create.html'
    def get_success_url(self):
        return reverse('projectapp:detail',kwargs={'pk':self.object.pk}) #프로젝트가 만들어질때 얻어오는 정보
class ProjectDetailView(DetailView,MultipleObjectMixin):
    model= Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by = 20 #게시판 아래에 연결되있는 게시글 들을 만들어준다

    #
    def get_context_data(self, **kwargs): #templates 에서 사용할 문맥 데이터를 제공해주는 함수 이다.
        article_list = Article.objects.filter() #조건에 맞는 게시글들만 filter
        return super().get_context_data(**kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list' #게시판 이미지를 담고 있는 이름
    template_name = 'projectapp/list.html'
    paginate_by = 20