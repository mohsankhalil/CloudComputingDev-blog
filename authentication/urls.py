from django.urls import path
from authentication import views

urlpatterns = [
    path("login/",views.LoginView, name="login"),
    path("sign-up/",views.RegistrationView,name="sign-up"),
    path("logout/",views.LogoutView,name="logout")
]
