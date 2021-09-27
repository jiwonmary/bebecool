from django.db import models

# Create your models here.
# ORM
# 데이터베이스의 데이터를 조회하거나 저장하기위해 원래는
# 쿼리(SQL)을 사용했지만 Django에서는
# 데이터베이스 테이블을 '모델화'해서 사용하고 쿼리들을
# Django 기준 python 코드로 처리하는 방법.

# ORM의 특징
# 개발자만의 쿼리(sql)을 만들기가 어렵다.
# 쿼리를 잘못 작성할 가능성이 낮아진다(간단한 명령에 한해서)
# DBMS를 변경(이관)할때 쿼리를 바꿀 필요가 없다.

# 모델 작성
# 질문, 답변 모델을 생성
# 질문모델
# subject : 질문의 제목
# content : 질문의 내용
# create_date : 질문을 작성한 일시

class Question(models.Model): #데이터베이스에 테이블 대신 만들었음/ 속성 제목, 내용, 작성일자.
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

# 답변모델
# question : 질문
# content: 답변의 내용
# create_date : e답변 작성 일시.
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 질문이 지워지면 답변까지 모두 지우기
    content = models.TextField()
    #답변에 작성된 내용 그대로 쓰기
    create_date = models.DateTimeField()
    # 답변작성 일지

