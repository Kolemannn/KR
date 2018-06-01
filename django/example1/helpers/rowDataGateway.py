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


	def getIid(self):
		return self.iid

	def getRowGroup(self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		return self.RowGroup

	def deleteRowGroup (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.delete()

	def getIid (self):
		return self.iid
    
	def setTitle (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.title = self.title
		self.RowGroup.save()

	def setTeacher (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.teacher = self.teacher
		self.RowGroup.save()

	def setDatetime (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.datetime = self.datetime
		self.RowGroup.save()

	def setLevel (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.level = self.level
		self.RowGroup.save()

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
			self.healthGroup = kwargs["healthGroup"]
		if "sectionStudent" in kwargs:
			self.sectionStudent = kwargs["sectionStudent"]
		self.RowStudent = []

	def getIid (self):
		return self.iid

	def findRowStudent(self):
		self.RowStudent = sm.Student.objects.filter( sectionStudent_id__exact = self.sectionStudent)
		return self.RowStudent

	def getRowStudent(self):
		self.RowStudent = sm.Student.objects.get( pk = self.iid )
		return self.RowStudent

	def deleteRowStudent (self):
		self.RowStudent = sm.Student.objects.get( pk = self.iid )
		self.RowStudent.delete()
	
    
	def setFioStudent (self):
		self.RowStudent = sm.Student.objects.get( pk = self.iid )
		self.RowStudent.fioStudent = self.fioStudent
		self.RowStudent.save()

	def setFaculty (self):
		self.RowStudent = sm.Student.objects.get( pk = self.iid )
		self.RowStudent.faculty = self.faculty
		self.RowStudent.save()

	def setHealthGroup (self):
		self.RowStudent = sm.Student.objects.get( pk = self.iid )
		self.RowStudent.healthGroup = self.healthGroup
		self.RowStudent.save()

	def setSectionStudent (self):
		self.RowStudent = sm.Student.objects.get( pk = self.iid )
		self.RowStudent.sectionStudent = self.sectionStudent
		self.RowStudent.save()

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
			self.studentAttend = int(kwargs["studentAttend"])
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
		pass
    
	def setDate (self):
		self.RowAttendance = sm.Attendance.objects.get( pk = self.iid )
		self.RowAttendance.date = self.date
		self.RowAttendance.save()

	def setAttendance (self):
		self.RowAttendance = sm.Attendance.objects.get( pk = self.iid )
		self.RowAttendance.attendance = self.attendance
		self.RowAttendance.save()

	def setStudentAttend (self):
		self.RowAttendance = sm.Attendance.objects.get( pk = self.iid )
		self.RowAttendance.studentAttend = self.studentAttend
		self.RowAttendance.save()