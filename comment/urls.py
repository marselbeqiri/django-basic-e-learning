from django.urls import path 
from comment import views


app_name = 'comment' 

urlpatterns = [
	path('<int:question_id>/add-comment/', views.add_comment, name='add_comment'), 
	path('<int:question_id>/approve/', views.comment_approve, name='comment_approve'),
	path('<int:question_id>/remove/', views.comment_remove, name='comment_remove'),

	path('<single_slug>/add-comment/', views.add_comment1, name='add_comment_main'), 
	path('<single_slug>/approve-main/', views.comment_approve1, name='comment_approve_main'),
	path('<single_slug>/remove-main/', views.comment_remove1, name='comment_remove_main'),
	
] 