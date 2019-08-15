from django.shortcuts import render

#Imports needed for Search  
from django.shortcuts import render
from django.db.models import Q
from poll.models import Question
from main.models import Tutorial

#Imports needed for Categories Nav Drop Down 
from main.models import Tutorial, TutorialCourse, TutorialCategory
 

from django.template.loader import render_to_string

def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(question_text__icontains=query)

            results= Question.objects.filter(lookups).distinct()
 
            lookups_main = Q(tutorial_title__icontains=query) | Q(tutorial_content__icontains=query)
            results_main= Tutorial.objects.filter(lookups_main).distinct()

            context={'results': results,
                     'submitbutton': submitbutton, 'results_main': results_main}

                               

            return render(request, 'search/search_result.html', context)


        else:
            return render(request, 'search/search.html')

    else:
        return render(request, 'search/search.html')



 


 
 
def Drop(request):
    marsel = 'beqiri'
    return render( request,"search/qeqe.html",{"marsel": marsel})


 