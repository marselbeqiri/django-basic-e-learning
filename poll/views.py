from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

# Importe per Coment 
#from .forms import  CommentForm

# Create your views here.
def index(request): 
	 latest_question_list = Question.objects.order_by('-question_pub_date')[:5]
	 return render(request, 'poll/index.html', 
	 			context = {"latest_question_list": latest_question_list})


def detail(request, question_id):  
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'poll/detail.html', {'question': question})


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    matching = Choice.objects.filter(question_id=question_id) # Marrim Choice qe kan PK vleren e question_ID
   
    results = [c.votes for c in matching]
    total = 0
    for x in results:
        total = x + total

    total_poll = 100/total

    return render(request, 'poll/result.html', {'question': question, 'total_poll': total_poll})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:result', args=(question.id,)))


"""
 # Shto koment 
 
def add_comment(request, question_id):
    post = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('poll:detail', question_id)
    else:
        form = CommentForm()
    return render(request, 'poll/add_comment.html', {'form': form})       


#@login_required
def comment_approve(request, question_id):
    comment = get_object_or_404(Comment, pk=question_id)
    comment.approve()
    return redirect('poll:detail', question_id)

def comment_remove(request, question_id):
    comment = get_object_or_404(Comment, pk=question_id)
    comment.delete()
    return redirect('poll:detail', question_id)

"""    