from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'
urlpatterns = [
    path('create/',ProfileCreateView.as_view(),name='create'),
    path('updata/<int:pk>',ProfileUpdateView.as_view(),name='update'), #저장할 pk 를 받아와야 한다 .
]