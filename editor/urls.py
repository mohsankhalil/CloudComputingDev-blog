from django.urls import path
from editor import views

urlpatterns = [
    path('login/',views.LoginViews,name="editor_login"),
    path("logout/",views.logoutView,name="logout_editor"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('add-blog/',views.AddBlogView,name="addblog"),
    path('edit-blog/<int:id>/',views.editPostView,name="edit-blog"),
    path('delete-blog/<int:id>/',views.deletePostView,name="delete-blog"),
]
