from django.forms import ModelForm

from profileapp.models import Profile

#forms 역할 웹 페이지에서 보여줄 내용의 형태 사용할것인지/안할것인지 형태를 만들어주는게 forms 의 역할이다.
class ProfileCreationsForm(ModelForm):
    class Meta: #image 에 pixel 이 정보(data) 인데 외적으로 사진을 표현하는게 사진의 촬영날짜 크기 등등 을 meta data 라고 한다.
        model = Profile #profile app 의 model 을 가져온다.
        fields = ['image','nickname','message'] #client 로 부터 받을 값들을 저장할 리스트 유저는 받지 않고 서버에서 비교 하면서 받아온다,


