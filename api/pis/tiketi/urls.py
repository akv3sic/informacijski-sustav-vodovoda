from django.urls import path
from .views import KvarView, Kvar

urlpatterns = [

    path('prijavakvara/', KvarView.as_view()),
    path("kvar/", Kvar.as_view()),
]