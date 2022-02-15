from django.urls import path
from .views import UliceView


urlpatterns = [

    path('getulice/',UliceView.as_view() )
]