from django.shortcuts import render, get_object_or_404, redirect
import store.models as sm
import store.forms  as fm
import os.path

class GroupGateway(object):
	
	def __init__(self, **kwargs):
		if "iid" in kwargs:
			self.iid = int(kwargs["iid"])
		if "title" in kwargs:
			self.title = kwargs["title"]
		if "teacher" in kwargs:
			self.teacher = kwargs["teacher"]
		if "datetime" in kwargs:
			self.datetime = kwargs["datetime"]
		if "level" in kwargs:
			self.level = kwargs["level"]
		self.RowGroup = []


	def getRowGroup(self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		return self.RowGroup

	def deleteRowGroup (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.delete()

	def editRowGroup (self):
		sm.Section.objects.filter(id = self.iid).update(title = self.title,teacher = self.teacher, datetime = self.datetime, level = self.level)
		

##################################################################################################

class StudentGateway(object):
	
	def __init__(self, **kwargs):
		if "iid" in kwargs:
			self.iid = int(kwargs["iid"])
		if "fioStudent" in kwargs:
			self.fioStudent = kwargs["fioStudent"]
		if "faculty" in kwargs:
			self.faculty = kwargs["faculty"]
		if "healthGroup" in kwargs:
			self.healthGroup = int(kwargs["healthGroup"])
		if "sectionStudent" in kwargs:
			self.sectionStudent = kwargs["sectionStudent"]
		if "contStudent" in kwargs:
			self.contStudent = kwargs["contStudent"]
		self.RowStudent = []


	def findRowStudent(self):
		self.RowStudent = sm.Student.objects.filter( sectionStudent_id__exact = self.sectionStudent)
		return self.RowStudent

	def getRowStudent(self):
		self.RowStudent = sm.Student.objects.get( pk = self.iid )
		return self.RowStudent

	def deleteRowStudent (self):
		self.RowStudent = sm.Student.objects.get( pk = self.iid )
		self.RowStudent.delete()
	
    
	def editRowStudent(self):
		sm.Student.objects.filter( pk = self.iid ).update(fioStudent = self.fioStudent, faculty = self.faculty,healthGroup = self.healthGroup,sectionStudent = self.sectionStudent,contStudent = self.contStudent )

##################################################################################################

class AttendanceGateway(object):
	
	def __init__(self, **kwargs):
		if "iid" in kwargs:
			self.iid = int(kwargs["iid"])
		if "date" in kwargs:
			self.date = kwargs["date"]
		if "attendance" in kwargs:
			self.attendance = kwargs["attendance"]
		if "studentAttend" in kwargs:
			self.studentAttend = kwargs["studentAttend"]
		if "reason" in kwargs:
			self.reason = kwargs["reason"]
		self.RowAttendance = []

	def findRowAttendan(self):
		self.RowAttendance = sm.Attendance.objects.filter( studentAttend_id__exact = self.studentAttend)
		return self.RowAttendance

	def getRowAttendance(self):
		self.RowAttendance = sm.Attendance.objects.get( pk = self.iid )
		return self.RowAttendance

	def deleteRowAttendance (self):
		self.RowAttendance = sm.Attendance.objects.get( pk = self.iid )
		self.RowAttendance.delete()

	def createRowAttendance (self):
		self.RowAttendance = sm.Attendance(date = self.date,attendance = self.attendance, studentAttend = self.studentAttend, reason = self.reason)
		self.RowAttendance.save()
    

###############################################################################################3

class TeacherGateway(object):
	
	def __init__(self, **kwargs):
		if "iid" in kwargs:
			self.iid = int(kwargs["iid"])
		if "fioTeacher" in kwargs:
			self.fioTeacher = kwargs["fioTeacher"]
		if "sport" in kwargs:
			self.sport = kwargs["sport"]
		if "contTeacher" in kwargs:
			self.contTeacher = (kwargs["contTeacher"])
		if "trackRecord" in kwargs:
			self.trackRecord = (kwargs["trackRecord"])
		if "grade" in kwargs:
			self.grade = int(kwargs["grade"])
		self.RowTeacher = []


	def getRowTeacher(self):
		self.RowTeacher = sm.Teacher.objects.get( pk = self.iid )
		return self.RowTeacher

	def deleteRowTeacher (self):
		self.RowTeacher = sm.Teacher.objects.get( pk = self.iid )
		self.RowTeacher.delete()

	def createRowTeacher (self):
		self.RowTeacher = sm.Teacher(fioTeacher = self.fioTeacher,sport = self.sport, contTeacher = self.contTeacher,trackRecord = self.trackRecord, grade = self.grade)
		self.RowTeacher.save()


	def editRowTeacher(self):
		sm.Teacher.objects.filter(pk = self.iid).update(fioTeacher = self.fioTeacher,sport = self.sport, contTeacher = self.contTeacher,trackRecord =  self.trackRecord,grade = self.grade )



    
