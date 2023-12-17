from django.urls import path
from blog import views

urlpatterns = [
    path('',views.HomeView,name="home"),
    path('about/',views.AboutView,name="about"),
    path('contact/',views.ContactView,name="contact"),
    path('post/<slug:pk>',views.PostView,name="post"),
    path('apply-form/',views.ApplyFormView,name="applyform")
]
