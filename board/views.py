from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import Questionform
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.
# 메인 페이지 작성
# 질문 목록 출력
# 21.09.17 김지원 작성
def index(request):
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리 추가 21.09.24
    # 페이지 입력 파라미터 추가

# 21.09.27
    # 페이징 처리 관련 템플릿 태그 속성
        # .count : 전체 게시물 개수
        # .per_page : 페이지당 보여 줄 게시물 개수
        # .page_range :  페이지 범위
        # number :  현재 페이지 번호
        # previous_page_number : 이전 페이지 번호
        # next_page_number : 다음 페이지 번호
        # has_previous : 이전 페이지 유무
        # has_next : 다음 페이지 유무
        # start_index : 현재 페이지 시작 인덱스
        # end_index : 현재 페이지 끝 인덱스

    # 페이지의 입력 파라미터 추가.
    page = request.GET.get('page', '1')
    # 조회기능
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리 기능 구현
    pagenator = Paginator(question_list, 10) # 페이지당 10개씩
    page_obj = pagenator.get_page(page)


        # question_list = Question.objects.order_by('-create_date')
        # Question  모델에서 객체를 참조하는데 / -가 붙어있으면 해당 객체를 기준으로 역순정렬
        # 역순으로 정렬해올 것.(객체는 create_date)
        # Question테이블에 객체 가져오기 odrder_by 정렬하기(오름)
        # 데이터 던지기 위한 변수  Question 제어
    context = {'question_list': page_obj}
    return render(request, 'question_list.html', context)
        #모델단에서 ->
        #최상위
        # return HttpResponse("떠.... 떳다?") #view에서 URl로 응답 (template, model 접근하지 않았다.
        #이벤트??? 자바

def detail(request, question_id):
        # urls.py 25 line , question_id question_list 글 목록들의 고유한 아이디 해당 로우의 아이디 값을 파라미터로 받아오기
        # 테이블의 데이터들을 글 목록 별로 상세내용을 보기위해 id값 받아와 처리
    question = Question.objects.get(id=question_id) # 아이디를 파라미터 값 받기
    return render(request, 'question_detail.html', {'question': question})

def test(request):
    #4. 요청
    return render(request, 'index.html')
    #어떤한 응답에 대해서 이 파이를 호출하라는 의미

#21.09.23 답변등록하기
#작성자 : 김지원
# get_object_or_404 : 사용자에게 보여지는 에러 메세지 제어 함수
#                        데이터의 유출을 막기 위한 방법.
# redirect : 페이지의 재 요청 데이터를 전송 후 페이지를 새로고침 하기 위함.
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # 다음과 같은 방식이 가능했던 이유는 question, answer 모델이 외래키로
    # 연결되어있기 때문.
# answer 모델 직업 사용하는 방법
    answer = Answer(question=question, content=request.POST.get('content'),
                    create_date=timezone.now())
    answer.save()
    return redirect('board:detail', question_id=question_id)
# 다른방법 제시
# 21.09.24김지원 질문등록 기능 구현 질문등록하기 버튼을 눌렸을 대 항목을 띄울려고 만든 과정
def question_create(request):
#post와 get 연결방식이 달라야한다 접속과 저장/ 일련의 행위 함꺼번에 처리
    if request.method == 'POST':
        form = Questionform(request.POST) # 질문등록에서 작성했던 내용이 form 변수에 저장
        if form.is_valid():                     # 입력받은 내용
            question = form.save(commit=False) # 저장하기 전에 멈추기 commit 중단! views에서 시간
            question.create_date = timezone.now() # 현재시간 저장
            question.save()
            return redirect('board:index')
    else:
        form = Questionform()
    return render(request, 'board/question_form.html', {'form': form})

#question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
#작성된 현재시간 가져오기
#return redirect('board:detail', question_id=question_id)
# redirect 어느 페이지로 갈 것인지에 대한 재 요청 view에 있는 detail 열기

