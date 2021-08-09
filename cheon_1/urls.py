"""cheon_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
#path('url주소/',include('연결시킬 앱에 url 주소 '))
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accountapp.urls')), #account url 로 들어가면 accountapp 로 이동할수 있게 url을 설정하라
    path('profile/',include('profileapp.urls')),
    path('article/',include('articleapp.urls')),
    path('comment/',include('commentapp.urls')),
] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) #미디어를 요청했을떄 알려줘야 한다. URL 과 ROOT 를
