from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('index_test/', views.index_test, name='index_test'),
    path('index_tests/', views.index_tests, name='index_tests'),

]
