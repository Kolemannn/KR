from django.shortcuts import render, get_object_or_404, redirect
import store.models as sm
import store.forms  as fm
from helpers.rowDataGateway import GroupGateway,StudentGateway,AttendanceGateway

class serviceGroup (object):
 	
 	def getGroups(request):
 		allgroups = sm.Section.objects.all()
 		return render (request, 'store/groups.html', locals())

 	def getGroup(request, iid):
 		gr =  GroupGateway(iid = iid)
 		g = gr.getRowGroup()
 		g_pk = gr.getIid()                                                              
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
 		form = fm.SectionForm (instance = g)
 		form = fm.SectionForm(request.POST)
 		if form.is_valid() :
 			g =  GroupGateway(iid = iid, title = form.cleaned_data['title'], teacher = form.cleaned_data['teacher'],datetime = form.cleaned_data['datetime'], level = form.cleaned_data['level'])
 			g.setTitle()
 			g.setTeacher()
 			g.setDatetime()
 			g.setLevel()
 			return redirect ('store:groups')
 		else :
 			return render (request, 'store/groupedit.html', locals())

 	def makeGroupdelete(request, iid):
 		g =  GroupGateway(iid = iid)
 		g.deleteRowGroup()
 		return redirect ('store:groups')

################################################################################################################3

class serviceStudent(object):
	
	def getStudents(request):
		allstudents = sm.Student.objects.all()
		return render (request, 'store/students.html', locals())
 	
	def getStudent(request, iid):
		st = StudentGateway( iid = iid)
		student = st.getRowStudent()
		st_pk = st.getIid()
		a = AttendanceGateway(studentAttend = st_pk)
		att = a.findRowAttendan()
		if request.method == "POST":
			form = fm.AttendanceForm(request.POST)
			if form.is_valid() :
				attAdd = form.save(commit = False)
				attAdd.date = form.cleaned_data['date']
				attAdd.attendance = form.cleaned_data['attendance']
				attAdd.studentAttend = form.cleaned_data['studentAttend']
				attAdd.save()
		else:
			form = fm.AttendanceForm()	
		return render (request, 'store/studentview.html', locals())

	def makeStudentedit(request, iid):
 		s = get_object_or_404( sm.Student, pk=iid)
 		form = fm.StudentForm (instance = s)
 		return render (request, 'store/studentedit.html', locals()) 

	def makeStudenteditPost (request, iid):
		s = get_object_or_404( sm.Student, pk=iid)
		form = fm.StudentForm (instance = s)
		form = fm.StudentForm(request.POST)
		if form.is_valid() :
			s = get_object_or_404 (sm.Student, pk=iid)
			s.fioStudent = form.cleaned_data['fioStudent']
			s.faculty = form.cleaned_data['faculty']
			s.healthGroup = form.cleaned_data['healthGroup']
			s.sectionStudent = form.cleaned_data['sectionStudent']
			s.save()
			return redirect ('store:students')
		else :
			return render (request, 'store/studentedit.html', locals())