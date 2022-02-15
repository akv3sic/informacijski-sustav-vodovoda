from django.urls import path
from .views import PrikljucakView

urlpatterns = [
   
    path('mojiprikljucci/', PrikljucakView.as_view())
    

]