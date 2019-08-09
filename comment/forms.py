from django import forms
from poll.models import Question

from comment.models import Comment_Poll, Comment_main

 
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment_Poll
        fields = ('author', 'text',)


class CommentFormMain(forms.ModelForm):

    class Meta:
        model = Comment_main
        fields = ('author', 'text',)


