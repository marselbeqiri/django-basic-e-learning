from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200, default=1) # category URL
	category_pic = models.ImageField(null=True, blank=True, upload_to="images_main/")

	class Meta:
		verbose_name_plural = "Categories" # kjo eshte per ne, do te shfaqet tek admin page. 

	def get_courses(self):
         return TutorialCourse.objects.filter(tutorial_category__tutorial_category=self.tutorial_category)	

	def __str__(self):
		return self.tutorial_category

class TutorialCourse(models.Model):
    tutorial_course= models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    # Tutorial_category, ben lidhjen e kesaj Tabele me Category. Nqs NUk ekziston kategoria, vendoset  vlera default. 
	# on_delete perdoret kur fshihet nje kategori dhe ne vend te asaj vendoset vlera default. 
    course_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Coursess in admin"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.tutorial_course
    
    def get_tutorials(self):
         return Tutorial.objects.filter(tutorial_course__tutorial_course=self.tutorial_course)

 

# Create your models here.
class Tutorial(models.Model): 
	tutorial_title = models.CharField(max_length=200)
	#Do te jete Titulli i Tutorialit 
	tutorial_content = models.TextField()
	# TextField sheben per te vendosur content
	# brenda dhe nuk i vendosim nje numer te 
	# caktuar karakteresh
	tutorial_published = models.DateTimeField("Date published", default=datetime.now())
	
	tutorial_course = models.ForeignKey(TutorialCourse, default=1, verbose_name="Courses", on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length=200, default=1)
	tutorial_pic = models.ImageField(null=True, blank=True, upload_to="images_main/")
	#Override 
	author= models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.tutorial_title

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)	