from django.urls import path
from .views import RegisterAdminView

urlpatterns = [
    path('register/', RegisterAdminView.as_view(), name='register-admin'),
]
