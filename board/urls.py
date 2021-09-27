from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
   path('', views.index, name='index'),
   path('<int:question_id>', views.detail, name='detail'),
   path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
   path('question/create/', views.question_create, name='question_create'),
   # path('url명, 뷰에서 가져올함수') 2단계 3 설정 어려워요. 잘 꼬인다.
    # path('', views.index), # 2. views 에서
    # path('testpage/', views.test), #url 주기 url에서 호출하는 함수 test
    # path('<int:question_id>', views.detail),
]