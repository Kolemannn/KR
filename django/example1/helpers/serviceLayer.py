from django.shortcuts import render, get_object_or_404, redirect
import store.models as sm
import store.forms  as fm
from helpers.rowDataGateway import GroupGateway,StudentGateway,AttendanceGateway, TeacherGateway
from helpers.visitor2 import *

from django.http import HttpResponseRedirect


class serviceGroup (object):
 	
 	def getGroups(request):
 		allgroups = sm.Section.objects.all()
 		return render (request, 'store/groups.html', locals())

 	def getGroup(request, iid):
 		gr =  GroupGateway(iid = iid)
 		g = gr.getRowGroup()
 		g_pk = g.pk                                                              
 		st = StudentGateway(sectionStudent = g_pk)
 		allst = st.findRowStudent()
 		return render (request, 'store/groupview.html', locals())

 	def makeGroupedit(request, iid):
 		g = get_object_or_404( sm.Section, pk=iid)
 		form = fm.SectionForm (instance = g)
 		return render (request, 'store/groupedit.html', locals())

 	def makeGroupeditPost(request, iid):
 		gr =  GroupGateway(iid = iid)
 		g = gr.getRowGroup() 
 		form = fm.SectionForm(request.POST)
 		if form.is_valid() :
 			g =  GroupGateway(iid = iid, title = form.cleaned_data['title'], teacher = form.cleaned_data['teacher'],datetime = form.cleaned_data['datetime'], level = form.cleaned_data['level'])
 			g.editRowGroup()
 			return redirect ('store:groups')
 		else :
 			return render (request, 'store/groupedit.html', locals())

 	def makeGroupdelete(request, iid):
 		g =  GroupGateway(iid = iid)
 		g.deleteRowGroup()
 		return redirect ('store:groups')

 	def makeGroupcreate (request):
 		form = fm.SectionForm(request.POST)
 		if form.is_valid() :
 			g =  sm.Section(title = form.cleaned_data['title'], teacher = form.cleaned_data['teacher'],datetime = form.cleaned_data['datetime'], level = form.cleaned_data['level'])
 			g.save()
 			return redirect ('store:groups')
 		else :
 			return render (request, 'store/groupcreate.html', locals())
        
 		
      
################################################################################################################3

class serviceStudent(object):
	
	def getStudents(request):
		allstudents = sm.Student.objects.all()
		return render (request, 'store/students.html', locals())
 	
	def getStudent(request, iid):
		st = StudentGateway( iid = iid)
		student = st.getRowStudent()
		st_pk = student.pk
		a = AttendanceGateway(studentAttend = st_pk)
		att = a.findRowAttendan()
		if request.method == "POST":
			form = fm.AttendanceForm(request.POST)
			if form.is_valid() :
				attAdd = AttendanceGateway(date = form.cleaned_data['date'], attendance = form.cleaned_data['attendance'], studentAttend = form.cleaned_data['studentAttend'], reason = form.cleaned_data['reason'])
				attAdd.createRowAttendance()
		else:
			form = fm.AttendanceForm()	
		return render (request, 'store/studentview.html', locals())

	def makeStudentedit(request, iid):
 		s = get_object_or_404( sm.Student, pk=iid)
 		form = fm.StudentForm (instance = s)
 		return render (request, 'store/studentedit.html', locals()) 

	def makeStudenteditPost (request, iid):
		s = StudentGateway( iid = iid)
		s = s.getRowStudent()
		form = fm.StudentForm(request.POST)
		if form.is_valid() :
			s = StudentGateway(iid = iid,fioStudent = form.cleaned_data['fioStudent'],faculty = form.cleaned_data['faculty'], healthGroup = form.cleaned_data['healthGroup'], sectionStudent = form.cleaned_data['sectionStudent'], contStudent = form.cleaned_data['contStudent']) 
			s.editRowStudent()
			return redirect ('store:students')
		else :
			return render (request, 'store/studentedit.html', locals())

#####################################################################################################

class serviceTeacher(object):
	
	def getTeachers(request):
		allteachers = sm.Teacher.objects.all()
		return render (request, 'store/teachers.html', locals())


	def getTeacher(request, iid):
		t = TeacherGateway(iid = iid)
		t = t.getRowTeacher()
		return render (request, 'store/teacherview.html', locals())

	def makeTeachercreate(request):
		form = fm.TeacherForm(request.POST)
		if form.is_valid() :
			g = TeacherGateway(fioTeacher = form.cleaned_data['fioTeacher'], sport = form.cleaned_data['sport'],contTeacher = form.cleaned_data['contTeacher'], trackRecord = form.cleaned_data['trackRecord'], grade = form.cleaned_data['grade'])
			g.createRowTeacher ()
			return redirect ('store:teachers')
		else: 
			return render (request, 'store/teachercreate.html', locals())
    
	def makeTeacheredit(request, iid):
 		t = get_object_or_404( sm.Teacher, pk=iid)
 		form = fm.TeacherForm (instance = t)
 		return render (request, 'store/teacheredit.html', locals())

	def makeTeachereditPost(request, iid):
		form = fm.TeacherForm(request.POST)
		if form.is_valid() :
			t = TeacherGateway(iid = iid, fioTeacher = form.cleaned_data['fioTeacher'], sport = form.cleaned_data['sport'],contTeacher = form.cleaned_data['contTeacher'], trackRecord = form.cleaned_data['trackRecord'], grade = form.cleaned_data['grade'])
			t.editRowTeacher()
			return redirect ('store:teachers')
		else: 
			return render (request, 'store/teacheredit.html', locals())

	def makeTeacherdelete(request, iid):
		t = TeacherGateway(iid = iid)
		t.deleteRowTeacher()
		return redirect ('store:teachers')

class serviceManager(object):
	def reportManager(request):
		if request.method == "POST":
			form = fm.ReportForm(request.POST)
			if form.is_valid() :
	 			st = StudReport(form.cleaned_data['attendance'],faculty = form.cleaned_data['faculty'], date = form.cleaned_data['date'])
	 			v = Manager()
	 			att = st.accept(v)

			form = fm.TeacherForm(request.POST)
			if form.is_valid() :
	 			st = TeachReport(datetime = form.cleaned_data['datetime'], trackRecord = form.cleaned_data['trackRecord'])
	 			v = Manager()
	 			sec = st.accept(v)

		else:
			form=fm.ReportForm()
			form_1=fm.TeacherForm()
		return render (request, 'store/userManager.html', locals())
		