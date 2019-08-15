from main.models import Tutorial, TutorialCourse, TutorialCategory
from poll.models import Question, Choice
#from django.template.loader import render_to_string

def categories_context(request):  
   # rendered = render_to_string('search/main_nav_drop.html', {'categories_drop': TutorialCategory.objects.all})
    

    def get_queryset(self):
       return 
    return {"rendered": TutorialCategory.objects.all,"rendered_question": Question.objects.all,
    		"random":Tutorial.objects.order_by('?')}



 