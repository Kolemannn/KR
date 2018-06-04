from django.contrib import admin

from .models import *


@admin.register (Section)
class SectionAdmin(admin.ModelAdmin):
 	pass

@admin.register (Student)
class StudentAdmin(admin.ModelAdmin):
 	pass


@admin.register (Attendance)
class AttendanceAdmin(admin.ModelAdmin):
	pass


@admin.register (Teacher)
class TeacherAdmin(admin.ModelAdmin):
	pass



	