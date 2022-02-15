from django.urls import path
from .views import MjestaView

urlpatterns = [
    path("getmjesta/", MjestaView.as_view())
    
]