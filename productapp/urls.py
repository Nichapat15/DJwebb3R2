from django.urls import path
from productapp import views

urlpatterns = [
    path('testbt', views.testbt, name='testbt'),

]
