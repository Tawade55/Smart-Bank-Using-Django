from django.urls import path
from .import views

app_name="userauths"

urlpatterns=[
	path("sign-up/",views.RegisterView,name="sign-up"),
	path("sign-out/",views.logoutView,name="sign-out"),
	path("sign-in/",views.LoginView,name="sign-in"),
]
