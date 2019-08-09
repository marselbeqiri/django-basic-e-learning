from django.db import models
from datetime import datetime

class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200, default=1) # category URL
	category_pic = models.ImageField(null=True, blank=True, upload_to="images_main/")

	class Meta:
		verbose_name_plural = "Categories" # kjo eshte per ne, do te shfaqet tek admin page. 

	def __str__(self):
		return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    # Tutorial_category, ben lidhjen e kesaj Tabele me Category. Nqs NUk ekziston kategoria, vendoset  vlera default. 
	# on_delete perdoret kur fshihet nje kategori dhe ne vend te asaj vendoset vlera default. 
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series


 

# Create your models here.
class Tutorial(models.Model): 
	tutorial_title = models.CharField(max_length=200)
	#Do te jete Titulli i Tutorialit 
	tutorial_content = models.TextField()
	# TextField sheben per te vendosur content
	# brenda dhe nuk i vendosim nje numer te 
	# caktuar karakteresh
	tutorial_published = models.DateTimeField("Date published", default=datetime.now())
	
	tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length=200, default=1)
	tuttorial_pic = models.ImageField(null=True, blank=True, upload_to="images_main/")
	#Override 
	def __str__(self):
		return self.tutorial_title

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)	