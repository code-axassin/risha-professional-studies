from django.urls import path
from apps.frontpage.views import frontpage, about
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("about/", about, name="about"),
    path("login/", auth_views.LoginView.as_view(template_name='frontpage/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='frontpage/logout.html'), name="logout"),

]