from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse

from .models import Questions, Answers

def index(request):
    latest_question_list = Questions.objects.order_by('-publish_date')[:5]
    context = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id):
    question = get_object_or_404(Questions,pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Questions,pk=question_id)

    try:
        selected_choice = question.answers_set.get(pk=request.POST['answers'])
    except (KeyError, Answers.DoesNotExist):
        # Redisplay voting form!
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message':"You didn't select an answer.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


    return HttpResponse("You're voting on question %s" % question_id)