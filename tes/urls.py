from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('tes/', views.index, name='index'),
    path('subtest2/', views.subtest2, name='subtest2'),
    path('subtest3/', views.subtest3, name='subtest3'),
    path('subtest4/', views.subtest4, name='subtest4'),
    path('', views.login, name='home'),
    path('finish/', views.finish, name='finish')
]