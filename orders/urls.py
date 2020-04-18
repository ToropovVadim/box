
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index_test/', views.index_test, name='index_test'),
    path('index_test/index_testt/', views.index_testt, name='index_testt'),

]
