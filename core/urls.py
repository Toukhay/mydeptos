from django.urls import path
from . import views
#Patron interno de las urls // core
urlpatterns = [
    path('',views.home, name='home'),
]   