import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    # __str__() 대화 형 프롬프트를 처리할 때 자신의 편의를 위해서 뿐만 아니라
    # Django의 자동 생성 관리자 전체에서 개체의 표현이 사용되기 때문에
    # 모델에 메소드를 추가하는 것이 중요함

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# 데이터베이스의 각 필드는 Field 클래스의 인스턴스로서 표현됨
#  CharField : 문자(character)필드를 표현
#  DateTimeField : 날짜와 시간(datetime) 필드를 표현함
#  => 이것은 각 필드가 어떤 자료형을 가질 수 있는지를 Django에게 말함

# 각각의 Field 인스턴스의 이름(question_text와 pub_date)은 기계가 읽기 좋은 형식의 데이터베이스 필드 이름임
# 이 필드명을 Python 코드에서 사용할 수 있으며, 데이터베이스에서는 컬럼명으로 사용할 것임

# Field 클래스의 생성자에 선택적인 첫번쨰 위치 인수를 전달해 사람이 일긱 좋은 이름을 지정할 수도 있음
# 이 방법은 Django의 내부를 설명하는 용도로 종종 사용되는데, 이는 마치 문서가 늘어난 것과 같은 효과를 가짐
# 만약 이 선택적인 첫번째 위치 인수를 사용하지 않으면, Django는 기계가 읽기 좋은 형식의 이름을 사용함
# -> 이 예제에서는, Question.pub_date에 한해서만 인간이 읽기 좋은 형식을 사용
#    그 외 다른 필드들은, 기계가 읽기 좋은 형태의 이름이라도 사람이 읽기에는 충분함

# 몇몇 Field 클래스들은 필수 인수가 필요함
# -> 예를 들어, CharField의 경우 max_length를 입력해 주어야 함
#   -> 이것은 데이터베이스 스키마에서만 필요한 것이 아닌 값을 검증할 때도 쓰임

# Field는 다양한 선택적 인수들을 가질 수 있음
# -> 이 예제에서는, default로 하여금 votes의 기본값을 0으로 설정

# ForeignKey를 사용한 관계설정
# -> 이 예제에서는, 각각의 Choice가 하나의 Question에 관계된다는 것을 Django에게 알려줌
# => Django는 다-대-일(many-to-one), 다-대-다(many-to-many), 일-대-일(one-to-one)과 같은 모든 일반 데이터베이스의 관계들를 지원함
