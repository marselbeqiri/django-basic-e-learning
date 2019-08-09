from django.urls import path, include 
from . import views 

app_name = "main"

urlpatterns = [
  	path("", views.homepage, name = "homepage"),
  	path("register/",views.register, name = "register"), # Kontroller per register.html
  	path("marsel/", views.marsel, name = "marsel"),
    path("logout/", views.logout_request, name = "logout"),
    # emrin e funksionit tek views nuk duhet ta shkruajm logout sepse ben override 
    # funksioniin 'logoout' tek django.contrib.auth
    path("login/", views.login_request, name = "login"),
   
    path("<str:single_slug>/", views.single_slug, name="single_slug"),

    # path('admin/', include('main.urls')),
    # Perdoren <,> per te treguar qe vlera brendda tyre eshte variabel 
]
