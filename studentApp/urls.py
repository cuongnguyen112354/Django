from django.urls import path
from . import views

urlpatterns = [
   path('', views.main, name='main'),
   path('list/', views.studentlist, name='studentList'),
   path('list/detail/<int:id>', views.studentdetail, name='studentDetail'),
]
