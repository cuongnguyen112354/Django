from django.http import HttpResponse
from django.shortcuts import render
from .models import Student


def studentlist(request):
   stdlist = Student.objects.all().values()
   return render(request, 'student_list.html', { 'stdList': stdlist })


def studentdetail(request, id):
   std = Student.objects.get(id=id)
   total_core = (std.qt1 + std.qt2*2 + std.mid*2 + std.final*5) / 10
   context = {
      'std': std,
      'total_core': total_core,
   }
   return render(request, 'detail.html', context)

def main(request):
   return render(request, 'main.html')

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      print(username, password)
      user = authenticate(request ,username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('main')
      return HttpResponse('Sai rồi!!!')
   else:
      return render(request, 'login.html')
   
def logoutPage(request):
   logout(request)
   return redirect('main')