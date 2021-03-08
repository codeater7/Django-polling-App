from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import Question, Choice

#  views ma k k garna paryo?
#  paila the model chaieeo
#  Render lee k k khanxa ( request, location of the template, )

# Get questions and display them
#  we can connect views to urls, we can render the json or someting 

# like in the shell, Question.objects.order_by('-ppub_data')
# context is the object 
def index(request):
  # Question Model .objects.all
  # Question.objects.order_by  (date but descending so - ) (we want only 5)

  latest_question_list = Question.objects.order_by('-pub_date')[:5]

  #  inorder to pass into the template, we pass it as an object common convention is to write context
  context = {'latest_question_list': latest_question_list}

    # last ko ma context falako ho
    return render(request, 'polls/index.html', context)






    # ###################################################################################################

# Show specific question and choices
#  question id, url bata ho hai
def detail(request, question_id):
  try:
    # pk= question_id will come from the url
    question = Question.objects.get(pk=question_id)
    context= {'question': question}
  except Question.DoesNotExist:
    raise Http404("Question does not exist")

    # PASS THE QUESTION AS THE DICTIONARY
  return render(request, 'polls/detail.html', context)







  # ###################################################################################################


# yo tala ko question_id  kaha bata aauxa huh??  
#  => uls.py ma path ('<int:question_id>' garako thio ni)

# Get question and display results
def results(request, question_id):
  # get_object_or_404 lee database ma herxa khojako payeana vani 404 result dinxa

  question = get_object_or_404(Question, pk=question_id)
  context={ 'question':question}
  return render(request, 'polls/results.html', context)

# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])  // form the detail.html page, choice_id
    question = get_object_or_404(Question, pk=question_id)

    # tala ko request.POST chai k ho? 
    # tyo detail ko value ={{choice.id }} ho 

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # if there is no selection, we are going to render the detail template and also pass error message
        # saying the selection was not made
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', context),
            'error_message': "You didn't select a choice.",
        
    else:
      #  if everything is going as usual, we are going to add one to vote and save in the database
      # later redirect
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))