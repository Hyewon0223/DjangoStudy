"""
   뷰를 호출하려면 이와 연결된 URL이 있어야 하는데, 이를 위해 URLconf가 사용된다.
   polls 디렉토리에서 URLconf를 생성하려면, urls.py라는 파일을 생성해야 한다.
"""

from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # detail()을 통해 url에 입력한 ID 값을 출력하게 되고, 해당 url을 통해 투표 서식을 보게 됨
    # 결과적으로 detail()엔 아래와 같은 값이 전달됨
    # detail(request=<HttpRequest object>, question_id=34)

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]