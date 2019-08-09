from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model): 
	question_text = models.CharField(max_length = 200)
	question_pub_date = models.DateTimeField('date published') # 'date published' is just human readable version of that field\
	model_pic = models.ImageField(null=True, blank=True, upload_to="images/")
	
	def __str__(self):
		return self.question_text


	def was_published_recently(self):
		return (self.pub_date >= timezone.now() - datetime.timedelta(days=1))	

	# Ben nje filtrim te komenteve te aprovuara
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) # on delete, merr vleren e dhene nqs nje question fshihet
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)	

	def __str__(self):
		return self.choice_text

# Modeli i Koment section

"""
class Comment(models.Model):
    post = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
        """