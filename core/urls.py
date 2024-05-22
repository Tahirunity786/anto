from django.urls import path
from core.views import engine


urlpatterns = [
    path('', engine, name="dashboard")
]
