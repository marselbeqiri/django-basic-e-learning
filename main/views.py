from django.shortcuts import render, redirect # Udhezon browserin te na dergoje menjeher ne URL e specifikuar
from django.http import HttpResponse
from .models import Tutorial, TutorialCourse, TutorialCategory
# Bejme Import Format nga Django 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Qe te behet logini duhet te bejme import keto.. 
from django.contrib.auth import login, logout, authenticate # authenticate password
# Bejme import messazhet nga django 
from django.contrib import messages
# Create your views here.

def single_slug(request, single_slug): # Mund te pranojme single_slug si variabel neper  URL path 
	# Me poshte kemi nje comprehensice List
	categories = [c.category_slug for c in TutorialCategory.objects.all()] # c.category_slug : do marri vetem URL (slug) dhe do i ruaj ne liste. Pra shmang te dhena qe sna duhen
	# c.category_slug => Bene te mudnur qe gjat ciklit for te zgjighen vetem category_slug ne objekte
	if single_slug in categories:
		matching_courses = TutorialCourse.objects.filter(tutorial_category__category_slug=single_slug)
		
		courses_urls = {}
		for m in matching_courses.all():
			part_one = Tutorial.objects.filter(tutorial_course__tutorial_course=m.tutorial_course).earliest("tutorial_published")
			courses_urls[m] = part_one.tutorial_slug
		
		return render(request,"main/category.html",{"part_ones": courses_urls})

	tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]

	if single_slug in tutorials:
		this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
		tutorials_from_courses = Tutorial.objects.filter(tutorial_course__tutorial_course=this_tutorial.tutorial_course).order_by('tutorial_published')
		this_tutorial_idx = list(tutorials_from_courses).index(this_tutorial)

		return render(request=request,
					template_name='main/tutorial.html',
					context={"tutorial": this_tutorial,
					"sidebar": tutorials_from_courses,
					"this_tut_idx": this_tutorial_idx})
	

	return HttpResponse(f"{single_slug} does not correspond to anything!")	
	


def homepage(request): 	
	return render(request=request,
				  template_name="main/categories.html",  # Tells django where to find specific template
				  context={"categories": TutorialCategory.objects.all})
				  # Context do: pass to Template. Dhe mund ti referohemi Objekteve Tutorial nepermjemt  variablit 'tutorials'		

def register(request):
	if  request.method == 'POST':
		form = UserCreationForm(request.POST) 
		# Our form is populated with POST information
		# Check if the form is Valid 
		if form.is_valid(): # Qe do te thote: A eshte mbushur  fomra me info ashtu sic duhet
			user = form.save() # user created
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			# Mesazh qe llogaria u krijua me sukses. Ky lloj mesazhi zakonisht perdoret vetem per user specifik, por ne mund ta perdorim si te duam
			# Pasi u krijua duam qe ky user te behet menjher login
			login(request, user)
			messages.info(request, f"You are loged in as  {username}")
			return redirect("main:homepage")
			# Shkon tek main, me pas homepage3
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
				#Tek f string duam te afishojme edhe key edhe mesazhin.  

	form = UserCreationForm
	return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})


def browse(request): 	
	return render(request=request,
				  template_name="main/browse_categories.html",  
				  context={"categories": TutorialCategory.objects.all})


def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username,password =password) 
			# (username = username,password =password => Parametrat duhen keshtu pasi jep error authenticate() takes from 0 to 1 positional arguments but 2 were given
			if user is not None:
				login(request, user)
				messages.info(request, f"You are loged in as  {username}")	
				return redirect("main:homepage")
			else: 
				messages.error(request, "Invalid username or Password [LOL]")	
		else: 
			messages.error(request, "Invalid username or Password [LOL]")			

	form = AuthenticationForm()
	return render(request, "main/login.html", {"form": form})


