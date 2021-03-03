"""
   뷰를 호출하려면 이와 연결된 URL이 있어야 하는데, 이를 위해 URLconf가 사용된다.
   polls 디렉토리에서 URLconf를 생성하려면, urls.py라는 파일을 생성해야 한다.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]