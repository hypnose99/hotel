from django.urls import path
from userauths.views import RegisterView

app_name = "userauths"

urlpatterns = [
    path("sign-up/", RegisterView, name="sign-up")
]