from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('tes/', views.index, name='index'),
    path('', views.login, name='login'),
]