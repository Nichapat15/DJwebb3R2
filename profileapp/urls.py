from django.urls import path
from profileapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.helloword, name='hello'),
    path('firstpage', views.firspage, name='firstpage'),
    path('secondpage', views.secondpage, name='secondpage'),
    path('thirdpage', views.thirdpage, name='thirdpage'),
    path('hnyPage', views.hnyPage, name='hnyPage'),
]