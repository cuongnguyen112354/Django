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