from django import template

# 21. 09. 27 김지원 템플릿 태그 커스터마이징
register = template.Library()
# 변수 r 라이브러리 등록

@register.filter()
# 라이브러리에 있는 메서드를 추가로 사용. sub라는 함수 호출될 때 f메서드가 함께 호출
def sub(value, arg):
    # value기본 값 이미있는 번호 값에서 받은 값 arg 빼기
    return value - arg

