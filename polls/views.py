from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic

from .models import Questions, Answers

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Questions.objects.order_by('-publish_date')[:5]

class DetailView(generic.DetailView):
    model = Questions   # Models required for generic views (which one will it be acting on)
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Questions   # Models required for generic views (which one will it be acting on)
    template_name = 'polls/results.html'

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