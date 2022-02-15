from django.urls import path, include
from .views import RacuniView, PotrosnjaView, PopisPrikljucaka, StanjeBrojilaView, broj_racuna

urlpatterns = [
   
    path('mojiracuni/', RacuniView.as_view()),
    path('potrosnja/', PotrosnjaView.as_view()),
    path('popisprikljucaka/', PopisPrikljucaka.as_view()),
    path('upisbrojila/', StanjeBrojilaView.as_view()),
    path('brojracuna/', broj_racuna)
    

]