from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('publications/<int:number_id>', views.publication, name='publication'),
    path('publications/<int:number_id>/comments', views.comments, name='comments'),
    path('', views.publications, name='publications'),
    path('publish', views.publish, name='publish'),
    path('contact', views.contact, name='contact'),
]
