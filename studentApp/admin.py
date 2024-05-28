from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
   list_display = ('mssv', 'ho_va_ten')
   
   def mssv(self, obj):
      return f'{obj.maso}'
   mssv.short_description = 'MSSV'
   
   def ho_va_ten(self, obj):
      return f"{obj.ho} {obj.ten}"
   ho_va_ten.short_description = 'Họ và Tên'
   
admin.site.register(Student, StudentAdmin)