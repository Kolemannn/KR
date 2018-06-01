# -*- coding: utf-8 -*-
from django import forms

from .models import *

class SectionForm(forms.ModelForm):
 	class Meta :
 		model = Section
 		fields = '__all__'
 		#exclude = ('Level',)
 		labels = {
 			'title': 'Название секции'
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
 			'sectionStudent' : 'Секция'
 			
 		}

class AttendanceForm (forms.ModelForm):
	class Meta :
		model = Attendance
		fields = '__all__'
		labels = {
 			'date'  	 	: 'Дата',
 			'attendance'  	: 'Присутствовал',
 			'studentAttend' : 'Студент'
 			
 		}
	
		