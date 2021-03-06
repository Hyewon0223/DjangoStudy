from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Question, Choice
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')

    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# 요청된 질문의 ID가 없을 경우 Http404 예외를 발생시킴
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST 는 키로 전송된 자료에 접근할 수 있도록 해주는 사전과 같은 객체
        # 이 경우, request.POST['choice'] 는 선택된 설문의 ID를 문자열로 반환
        # request.POST 의 값은 항상 문자열

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
        # 만약 POST 자료에 choice 가 없으면,
        # request.POST['choice'] 는 KeyError 가 일어남
        # 위의 코드는 KeyError 를 체크하고, choice가 주어지지 않은 경우에는
        # 에러 메시지와 함께 설문조사 폼을 다시 보여줌

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))