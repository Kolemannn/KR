from django.shortcuts import render, get_object_or_404, redirect
from abc import ABCMeta, abstractmethod
import store.models as sm
import store.forms  as fm
import os.path


class Visitor(metaclass=ABCMeta):
	@abstractmethod
	def visit(self, rep) -> None:
		pass


class Report(metaclass=ABCMeta):
	@abstractmethod
	def accept(self, visitor: Visitor) -> None:
		pass



class StudReport(Report):
	def __init__(self, Boolean, faculty, date) -> None:
		self.Boolean = Boolean
		self.faculty = faculty
		self.date = date
		self.att = []
    
	def accept(self, visitor: Visitor)-> None:
		att = visitor.visit(self)
		return att

	def createStudentReport(self)-> None:
		att = sm.Attendance.objects.filter(attendance = self.Boolean)
		att = att.filter(studentAttend__faculty = self.faculty)
		self.att = att.filter(date = self.date)
		return self.att

class TeachReport(Report):
	def __init__(self, datetime,trackRecord) -> None:
		self.datetime = datetime
		self.trackRecord = trackRecord
		self.sec = []
    
	def accept(self, visitor: Visitor)-> None:
		sec = visitor.visit(self)
		return sec

	def createTeacherReport(self)-> None:
		sec = sm.Section.objects.filter(datetime__contains = self.datetime)
		self.sec = sec.filter(teacher__trackRecord__contains = self.trackRecord)
		return self.sec

class Manager(Visitor):
	
	def visit(self, rep: Report) -> None:
		if isinstance (rep, StudReport):
			att = rep.createStudentReport()
			return att
		elif isinstance(rep, TeachReport):
			sec = rep.createTeacherReport()
			return sec


		



	