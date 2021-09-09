#배포 할때 사용할 설정들

from .base import *

env_list = dict()

local_env = open(os.path.join(BASE_DIR,".env"))
'''
os 운영체제 마다 경로가 다 다르기 때문에 그것을 제공하기 위한 라이브러리 
os.path.join(BASE_DIR,".env") 
최상의 폴더 인 프로젝트 폴더에서 .env 파일을 찾는다
'''

while True:
    line = local_env.readline() #한줄 한줄 씩 읽는 readline method
    if not line:
        break
    line = line.replace('\n','') #줄바꿈 줄 찾아서 공백으로 바꾸기
    start = line.find('=') # '=' 처음 나오는 문자의 인덱스 찾기
    key = line[:start] # = 이전에는 key
    value = line[start+1:] # = 이후에는 value
    env_list[key] = value #dict 로 만들기

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! 배포 환경에서는 숨겨야 하는 키 + 분리 시킬 예정
SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #실제 배포 할때는 False 로 바꿔줘야 한다.

ALLOWED_HOSTS = ["*"] #모든 host 를 접속 가능하도록 설정하는것이다.


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #mysql 에서 분화 되어 나온게 mariadb 이다
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'fkaus132^^',
        'HOST': 'mariadb', #네트워크 를 사용할때 container 에서 mariadb 를 도메인처럼 사용하기 위해서  즉 container name 이 들어간다.
        'PORT': '3306',
    }
}
