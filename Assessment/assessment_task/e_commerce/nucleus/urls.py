from django.urls import path

from . import views

app_name = "nucleus"

urlpatterns = [
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_in/", views.user_sign_in, name="sign_in"),
    path("sign_out/", views.user_sign_out, name="sign_out"),

    path("profile/<int:pk>/", views.UserProfile.as_view(), name="profile"),
    path("profile/<int:pk>/update_details/", views.user_update_details, name="update_details"),
    path("profile/<int:pk>/change_password", views.change_password, name="change_password"),
]
