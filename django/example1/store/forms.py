# -*- coding: utf-8 -*-
from django import forms

from .models import *

class SectionForm(forms.ModelForm):
 	class Meta :
 		model = Section
 		fields = '__all__'
 		#exclude = ('Level',)
 		labels = {
 			'title'		: 'Название секции',
 			'teacher'	: 'Преподаватель',
 			'datetime'	: 'Время занятий',
 			'level'		: 'Уровень'
 		}
 		
 		

class StudentForm(forms.ModelForm):
 	class Meta :
 		model = Student
 		fields = '__all__'
 		#exclude = ('Level',)
 		labels = {
 			'fioStudent'  	 : 'Ф.И.О',
 			'faculty'  	     : 'Факультет',
 			'healthGroup' 	 : 'Группа здоровья',
 			'sectionStudent' : 'Секция',
 			'contStudent'	 : 'Телефон'
 		}

class AttendanceForm (forms.ModelForm):
	class Meta :
		model = Attendance
		fields = '__all__'
		labels = {
 			'date'  	 	: 'Дата',
 			'attendance'  	: 'Присутствовал',
 			'studentAttend' : 'Студент',
 			'reason'		: 'Причина'
 		}
	
class TeacherForm (forms.ModelForm):
	class Meta :
		model = Teacher
		fields = '__all__'
		labels = {
 			'fioTeacher'  	: 'Ф.И.О',
 			'sport'  		: 'Вид спорта',
 			'contTeacher' 	: 'Телефон',
 			'trackRecord'	: 'Достижения',
 			'grade'			: 'Грейд'
 		}
		
class ReportForm(forms.Form):
	attendance = forms.BooleanField(label = 'Присутствовал',required=False)
	faculty = forms.CharField(label = 'Кафедра')
	date = forms.DateField( label = 'Дата')

class TeacherForm(forms.Form):
	datetime = forms.CharField(label = 'День недели')
	trackRecord = forms.CharField(label = 'Достижение')