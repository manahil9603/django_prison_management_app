from django.contrib import admin
from django.urls import path
from home import views
from .views import prisoner
from .views import visitor
from .views import guard

urlpatterns = [
   
   path("", views.index, name='home'),
   path("prisoner", views.prisoner, name='prisoner'),
   path("visitor", views.visitor, name='visitor'),
   path("guard", views.guard, name='guard'),

]
