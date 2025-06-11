from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('grades/', views.grades, name='grades'),
    path('add_grade/', views.add_grade, name='add_grade'),
    path('absences/', views.absences, name='absences'),
    path('add_absence/', views.add_absence, name='add_absence'),
]
