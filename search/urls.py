from django.urls import path 

from search import views
 
app_name = 'search' 

urlpatterns = [
	path('',views.search, name='search'),
	path('search-result/', views.search, name='search_results'),
 	path('drop/', views.Drop, name='drop'),

 ] 
