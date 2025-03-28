# from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice
import datetime
# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the Last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {"latest_question_list": latest_question_list}
    # output = ",<br> ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context,request))
    # return render(request,'polls/index.html',context)

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = '<html lang = "en"> <body> It is now %s.</body></html>' %now
#     return HttpResponse(html)


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# def detail(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, "polls/detail.html", {"question":question})
#     # return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
   
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/results.html', {"question":question})
#     # response = "You're looks at the results of questions %s"
#     # return HttpResponse(response % question_id)



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


