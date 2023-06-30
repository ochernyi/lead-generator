from django.contrib.auth.views import LogoutView
from django.urls import path

from lead.views import (
    Index,
    UserCreateView,
    login_view,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

app_name = "lead"
