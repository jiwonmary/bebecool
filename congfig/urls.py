"""congfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #경로등록
from django.urls import path, include
#from board import views
# 추가할 앱에 대해서만 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls'))
   # path('url명, 뷰에서 가져올함수') 2단계 3 설정 어려워요. 잘 꼬인다.
    # path('', views.index), # 2. views 에서
    # path('testpage/', views.test), #url 주기 url에서 호출하는 함수 test
    # path('<int:question_id>', views.detail),
]