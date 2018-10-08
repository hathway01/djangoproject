from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("q1/", views.question1, name='question'),
    path("q2/", views.question2, name='question'),
    path("q3/", views.question3, name='question'),
    path("q4/", views.question4, name='question'),
    path("q5/", views.question5, name='question'),
]
