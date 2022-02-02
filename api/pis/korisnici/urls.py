from django.urls import path
from .views import registerUsers, loginUsers, userLogout, UserUpdate

urlpatterns = [
    path('registracija/', registerUsers),
    path('prijava/', loginUsers),
    path('odjava/', userLogout),
    path('profil/', UserUpdate.as_view())
    

]