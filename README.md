# Django 로 Pinterst 따라 만들기 

## Pinterst?
- 핀터레스트(Pinterest)는 이용자가 스크랩하고자 하는 이미지를 포스팅하고 다른 이용자와 공유하는 소셜 네트워크 서비스이며, 명칭은 핀(Pin)과 인터레스트(Interest)의 합성어이다.

## 기술 스택 
- 언어 : Python , HTML , CSS , JS 
- 프레임워크 : Django , bootstrap
- 외부소스 및 디자인 : Naver Font , Google Fonts, Icons , MagicGrid

## 개발툴 
- Pycharm Pro


## 프로젝트 기능 설명 

### accountapp
- django 에서 제공하는 User Model 을 사용한 회원가입 , 회원 정보 보기 , 회원 정보 수정 , 회원 삭제
- 회원가입 을 실제로 적용해볼수 있는 Login , Logout 기능 만들기
- 로그인 할때만 적용할수 있는 Login_Required , 소유자 여부 판별 decorator 제작

### profileapp 
- User model 과 일대인 관계를 맺어 유저별 프로필 기능 개발
- 프로필 제작 (프로필 이미지업로드 , 프로필 이름 , 닉네임 , 계정 설명)
- 프로필 업데이트 (프로필 이미지업로드 , 프로필 이름 , 닉네임 , 계정 설명)

### articleapp
- 게시물 작성 , 게시물 조 , 게시물 업데이트 , 게시물 삭제 , 게시글 리스트 보기
- 게시물 +댓글을 한번에 보기위해서 사용하는 FormMixin 기능 사용

### commentapp
- 게시글에 사용자가 작성할수 있는 댓글 기능 작성
- 댓글 생성 , 댓글 삭제 기능 제작

### projectapp
- 게시글을 하나의 프로젝트로 사용할수 있게 제작
- 프로젝트 생성 , 프로젝트 조회 , 프로젝트 리스트 조회
- 프로젝트에 대해 구독 기능도 생성 (login 한 사람만 볼수 있음)

### subscribeapp
- 유저가 구독한 프로젝트의 게시글을 리턴하는 구독 기능
-  구독 되어있을때는 구독 취소 / 구독이 안되어있으면 구독 됨

### likeapp
- 게시글에서 좋아요 기능 , 카운트 증가 (좋아요는 한번만) 

