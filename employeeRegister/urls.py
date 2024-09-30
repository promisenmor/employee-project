from . import views
from django.urls import path

urlpatterns = [
    path('', views.employee_list, name='home'),
    path('forms/', views.employee_form, name='forms'),
    path('delete/', views.employee_delete, name='delete')
]