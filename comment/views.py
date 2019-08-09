from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from poll.models import Question

from comment.models import Comment_Poll, Comment_main
from comment.forms import  CommentFormMain, CommentForm

from django.urls import reverse

from main.models import Tutorial



 #_____________View per Poll_________________________ 
 
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
    return render(request, 'comment/add_comment.html', {'form': form})       


#@login_required
def comment_approve(request, question_id):
    comment = get_object_or_404(Comment_Poll, pk=question_id)
    comment.approve()
    return redirect('poll:detail', comment.post.id)

def comment_remove(request, question_id):
    comment = get_object_or_404(Comment_Poll, pk=question_id)
    comment.delete()
    return redirect('poll:detail', comment.post.id)


#__________________View per main_________________________________

def add_comment1(request, single_slug):
   # if single_slug in tutorials:
   #      this_tutorial = Tutorial.objects.get(tutorial_slug = single_slug)
   #      #global tutorial_15 = this_tutorial.id 

    post = get_object_or_404(Tutorial, tutorial_slug = single_slug)
    
    if request.method == "POST":
        form = CommentFormMain(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('main:single_slug', single_slug)
    else:
        form = CommentFormMain()
    return render(request, 'comment/add_comment.html', {'form': form})       


#@login_required
def comment_approve1(request, single_slug):
    comment = get_object_or_404(Comment_main, pk=single_slug)
    comment.approve()
    return redirect('main:single_slug', comment.post.tutorial_slug)

def comment_remove1(request, single_slug):
    comment = get_object_or_404(Comment_main, pk=single_slug)
    comment.delete()
    return redirect('main:single_slug', comment.post.tutorial_slug)