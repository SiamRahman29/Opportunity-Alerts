from django.urls import path
from . import views

app_name = "competition"

urlpatterns = [
    path('<int:pk>/', views.detail, name = 'detail'),
]
