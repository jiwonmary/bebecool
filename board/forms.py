from django import forms
from board.models import Question, Answer

#폼
# 페이지 요청 시 전달되는 파라미터들을 쉽게 관리하기 위해 사용하는 클래스
# 필수 파라미터의 값이 누락되지 않았는지 형식은 적절한지를 검증할 목적으로 사용
# HTML의 자동생성, 연결된 모델을 이용해서 데이터를 저장할 수도 있음
# 메타클래스(프레임워크에서 주로 사용)
# 클래스 안의 클래스
# 메타킄래스의 사용이유 : 클래스를 동적으로 사용하고 싶을 때
#                       클래스를 원하는 방향으로 쉽게 컨트롤하고 싶을 때.(커스텀 메타클래스)
class Questionform(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델의 연결(모델폼 상속)
        fields = ['subject', 'content'] # QuestionFrom 클래스에서 사용
                                        # Question 모델의 속성
        # widgets = {     # 출력할 폼에 스타일 지정 Textarea 커다란 입력 창
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        labels ={
            'subject': '제목',
            'content': '내용',
        }