from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index_page'),
    path('create-employee/',views.employee_manage,name='create-employee'),
    path('update-employee/<str:pk>',views.employee_manage,name='update-employee'),
]