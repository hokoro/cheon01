"""
Django settings for cheon_1 project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent
'''
settings.py 에 운영체제의 경로를 나타낸다
이떄 parent parent 부모의 부모 경로 최상위 프로젝트 이다
'''
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
DEBUG = True

ALLOWED_HOSTS = ["*"] #모든 host 를 접속 가능하도록 설정하는것이다.


# Application definition

#연결시킬 앱의 이름 #app 을 만들면 무조건 app 등록
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accountapp',
    'bootstrap4',
    'profileapp',
    'articleapp',
    'commentapp',
    'projectapp',
    'subscribeapp',
    'likeapp',
]

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR:'danger' #메세지의 에러 tag 를 커스터 마이징 을 할수 있다.
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cheon_1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cheon_1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/' #static 관련 url 이 들어왔을떄 경로를 설정한다.

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles') #basedir 로 가서 staticfiles 라는 폴더를 정적 루트로 사용한다.

STATICFILES_DIRS = [
    BASE_DIR / "static",
    #프로 젝트 폴더에서 static 폴더를 찾아서 전체 프로젝트 에 적용하여 인식한다.
    #static 이라는 css 정적 파일을 찾기 위해서

]

MEDIA_URL = '/media/' #static 관련 url 이 들어왔을떄 경로를 설정한다.

MEDIA_ROOT = os.path.join(BASE_DIR,'media') #profile app 부터는 이미지를 업로드 받기 때문에 지정해줘야 한다

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#login redirect 경로



LOGIN_REDIRECT_URL = reverse_lazy('articleapp:list') #로그인을 했을시 재연결 시킬
LOGOUT_REDIRECT_URL = reverse_lazy('accountapp:login') #로그아웃 시킬시 재연결