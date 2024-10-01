from . import views
from django.urls import path

urlpatterns = [
    path('', views.employee_form, name='form'),
    path('list/', views.employee_list, name='list'),
    #path('delete/', views.employee_delete, name='delete')
]