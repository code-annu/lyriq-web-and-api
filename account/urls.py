from django.urls import path
from .views import *

app_name = "account"
urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("success/", success_view, name="success"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("generate-token/", generate_token_view, name="generate_token"),

]