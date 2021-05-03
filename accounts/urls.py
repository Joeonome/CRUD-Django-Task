from django.urls import path

from .views import SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', auth_views.PasswordChangeView.as_view(), name="password_reset_form")
]