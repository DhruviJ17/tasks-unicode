from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.solutionform, name='form'),
    path('solution/<int:num1>/<int:num2>/', views.solution, name='solution'),
    path('user/', views.queryuser, name='user'),
    path('query/<username>/', views.Query, name='query'),
    path('repo/', views.repoQuery, name='repo'),
    path('folo/', views.foloQuery, name='folo'),
    path('topthree/', views.topthree, name='topthree'),
]