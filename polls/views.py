from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request=request, template_name='polls/detail.html', context={'question': question})


def results(request, question_id):
    question = get_object_or_404(klass=Question, pk=question_id)
    return render(request=request, template_name='polls/results.html', context={'question': question})


def vote(request, question_id):
    question = get_object_or_404(klass=Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request=request,
            template_name='polls/detail.html',
            context={'question': question, 'error_message': 'You didn\'t select a choice.'}
        )
    else:
        selected_choice.votes = F(name='votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(redirect_to=reverse('polls:results', args=(question_id,)))
