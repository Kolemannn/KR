from django.shortcuts import render, get_object_or_404, redirect
from abc import ABCMeta, abstractmethod
import store.models as sm
import store.forms  as fm
import os.path


class Spy(metaclass=ABCMeta):
	'''
		создатель отчётов
	'''

	@abstractmethod
	def visit(self, facility) -> None:
		'''
			создать отчёт о...
		'''
		pass


class Report(metaclass=ABCMeta):
	'''
		создаваемый отчёт
	'''

	@abstractmethod
	def accept(self, reportCreator: ReportCreator) -> None:
		'''
			принять создателя отчётов
		'''
		pass



class StudentReport(Report):
	'''
		отчёт для студентов
	'''
	def __init__(self, Boolean, faculty, date) -> None:
		self.Boolean = Boolean
		self.faculty = faculty
		self.date = date
    
	def accept(self, reportCreator: ReportCreator)-> None:
		ReportCreator.visit(self)

	def createStudentReport(self)-> None:
		att = sm.Attendance.objects.filter(attendance = self.Boolean)
		att = att.filter(studentAttend__faculty = self.faculty)
		att = att.filter(date = self.date)
		return att

class TeacherReport(Report):
	'''
		отчёт для преподавателей
	'''
	def __init__(self, datetime,trackRecord) -> None:
		self.datetime = datetime
		self.trackRecord = trackRecord
    
	def accept(self, reportCreator: ReportCreator)-> None:
		ReportCreator.visit(self)

	def createTeacherReport(self)-> None:
		sec = sm.Section.objects.filter(datetime__contains = self.datetime)
		sec = sec.filter(teacher__trackRecord__contains = self.trackRecord)
		return sec


class Manager(ReportCreator):
	
	def visit(self, report: Report) -> None:
		if isinstance (report, StudentReport):
			report.createStudentReport()
		elif isinstance(report, TeacherReport):
			report.createTeacherReport()


		



	