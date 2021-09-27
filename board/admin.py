from django.contrib import admin
from.models import Question  #겉은경로에 있는 모델 찾아라
# admin이라는 클래스에서 가져옴.
# Register your models here.
admin.site.register(Question)