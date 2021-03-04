from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    # output = ', '.join([q.question_text for q in latest_question_list]) //// 첫번째 방법

    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context) #  context는 템플릿에서 쓰이는 변수명과 Python 객체를 연결하는 사전형 값입니다.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question}) # 단축기능

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Chocie.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {'question': question, 
            'error_message': "You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button. 
        # 위의 Python 설명에서 지적했듯이 POST 
        # 데이터를 성공적으로 처리한 후에는 항상 HttpResponseRedirect를 반환해야 합니다. 이 팁은 Django에만 국한되지 않습니다.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))