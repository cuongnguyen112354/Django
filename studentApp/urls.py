from django.urls import path
from . import views

urlpatterns = [
   path('', views.main, name='main'),
   path('list/', views.studentlist, name='studentList'),
   path('list/detail/<int:id>', views.studentdetail, name='studentDetail'),
   path('login/', views.loginPage, name='login'),
   path('logout/', views.logoutPage, name='logout')
]
