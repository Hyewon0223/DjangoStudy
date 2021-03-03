"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# include() : 다른 URLconf들을 참조할 수 있도록 도와줌
# -> Django가 include()를 만나게되면, URL의 그 시점까지 일치하는 부분을 잘라내고,
#    남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달한다.
# -> inclue() 덕분에 URL을 쉽게 연결할 수 있다. polls 앱에 그 자체의 URLconf(polls/urls.py)가 존재하는 한,
#    그 어떤 다른 root 경로에 연결하더라도, 앱은 여전히 잘 동작할 것이다.
# -> 그렇다면 include()는 언제 사용해야 하는가?
#    -> 다른 URL 패턴을 포함할 때마다 항상 include()를 사용해야 한다.
#    -> admin.site.urls가 유일한 예외!

# path() : 2개의 필수 인수인 route와 view, 2개의 선택 가능한 인수로 kwargs와 name까지 모두 4개의 인수가 전달됨
# -> route : URL 패턴을 가진 문자열
#           -> 요청이 처리될 때, Django는 urlpatterns의 첫번째 패턴부터 시작해, 일치하는 패턴을 찾을 때까지 요청된 URL을 각 패턴과 리스트의 순서대로 비교
#           -> 패턴들은 GET이나 POST의 매개 변수들, 혹은 도메인 이름을 검색하지 않음
#           -> 예를 들어, https://www.example.com/myapp/과 https://www.example.com/myapp/?page=3과 같은 요청에도 URLconf는 myapp/ 부분만 신경씀
# -> view : 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째 인수로 하고,
#           경로로부터 <캡처된> 값을 키워드 인수로 하여 특정 view 함수를 호출
# -> kwargs : 임의의 키워드 인수들은 목표한 view에 사전형으로 전달
# -> name : URL에 이름을 지으면, 템플릿을 포함해 어디서나 명확하게 첨조할 수 있음
#           이러한 기능을 이용해, 단 하나의 파일만 수정해도 프로젝트 내의 모든 URL 패턴을 바꿀 수 있도록 도와줌
