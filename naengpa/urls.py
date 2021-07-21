# 서브앱의 urls.py
# 같은 위치의 view.py 함수로 연결 역할 (path)
# view 식별 못할 시 import

from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Recipe',views.RecipeViewSet)

# 프로젝트 폴더 urls.py 내 urlpatterns 처럼 경로 추가 가능
urlpatterns = [
    path('', include(router.urls)),
    path('main/',views.index,name='index'),
]