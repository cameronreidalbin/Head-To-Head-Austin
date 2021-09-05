from django.urls import path
from . import views

urlpatterns = [
    path('', views.matchup, name='matchup'),
    path('results/', views.results, name='results'),
]