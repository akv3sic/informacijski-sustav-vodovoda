from django.urls import path
from .views import CjenovnikView

urlpatterns = [
   
    path('cjenovnik/', CjenovnikView.as_view()),
    
    

]