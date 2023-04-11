from django.urls import path
from . import views

urlpatterns=[
    
path('',views.index,name='index'),
path('courses',views.course,name='course'),
path('Gallery',views.gallery,name='gallery'),
path('placement',views.placement,name='placement'),
path('contact',views.contact,name='contact')
]