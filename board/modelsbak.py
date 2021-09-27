from django.db import models

# Create your models here. #테이블 만들기/ 속성 /질문, 답변 테이블
# ORM
# 데이터베이스의 데이터를 조회하거나 저장하기 위해 원래는
# 쿼리(SQL)을 사용했지만 Django에서는
#데이터베이스 테이블을 '모델화(클래스화)'해서 사용하고 쿼리들을
# Django 기준 python 코드로 처리하는 방법.

# ORM의 특징
# 개발자만의 커리(sql)을 만들기가 어렵다.
# 쿼리를 잘못 작성할 가능성이 낮아진다. (간단한 명령에 한해서)
# DBMS를 변경(이관)할 때 쿼리를 바꿀 필요가 없다. 데이터 주머니 :모델

# ORM 관점에서 보면 모델 작성
# 질문, 답변 모델을 생성
# 질문모델
# subject : 질물의 제목
# content : 질문의 내용
# create_date : 질문을 작성한 일시
#질문모델: class 형태 #변수명 정의

class Question(models.Model):
    subject = models.CharField(max_length=200) #문자의 글자 수를 제어할 때
    content = models.TextField()  #제목: 문자의 제한 없이 사용
    create_date = models.DateTimeField()  #문자형으로 되어있을 때도 많음. 데이터형이 편함. 날짜컨트롤 어려움 yymmdd


# 답변모델 // 키 값은 테이블에 데이터들을 식별하는 고유한 값.
# question : 질문 (모델에 대한 속성)컬럼 질문모델과 연결하기 위한 속성
# content : 답변의 내용
# create_date : e답변 작성 일시.(네이버 지식인)

class Answer(models.Model): #qna 상속기능을 이용해서 모델기능 사용
    #질문이 삭제되면 답변도 함께 삭제. 답변을 등록할 때 해당 질문과 키 값을 통해 연동. 키 값이 자동으로 증가(시컨스)id(기본키)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #다른 테이블과 연결하는 키 / 어느 테이블과 연결... 삭제도
    content = models.TextField()
    create_date = models.DateTimeField() #테이블이 다르면 명이 같아도 된다.
