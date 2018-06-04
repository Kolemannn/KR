from django.shortcuts import render, get_object_or_404, redirect
from helpers.multirequest import multirequest
from helpers.serviceLayer import serviceGroup, serviceStudent, serviceTeacher, serviceManager

from .models import *
from .forms import *

############################Section########################################
def groups(request):	
    return serviceGroup.getGroups(request)

def group (request, iid):
	return serviceGroup.getGroup(request, iid)

@multirequest
def groupedit(request, iid):
	return serviceGroup.makeGroupedit(request, iid)
		
@groupedit.POST
def groupedit (request, iid):
	return serviceGroup.makeGroupeditPost(request, iid)	

def groupdelete( request, iid):
	return serviceGroup.makeGroupdelete(request, iid)

def groupcreate(request):
	return serviceGroup.makeGroupcreate(request)
###########################Students############################

def students(request):
    return serviceStudent.getStudents(request)
    

def student (request, iid):
	return serviceStudent.getStudent(request, iid)


@multirequest
def studentedit(request, iid):
	return serviceStudent.makeStudentedit(request, iid)	 

@studentedit.POST
def studentedit (request, iid):
	return serviceStudent.makeStudenteditPost(request, iid)
	
		
#######################################################################

def teachers (request):	
    return serviceTeacher.getTeachers(request)

def teacher(request, iid):
	return serviceTeacher.getTeacher(request, iid)

def teachercreate(request):
	return serviceTeacher.makeTeachercreate(request)

@multirequest
def teacheredit(request, iid):
	return serviceTeacher.makeTeacheredit(request, iid)	

@teacheredit.POST
def teacheredit (request, iid):
	return serviceTeacher.makeTeachereditPost(request, iid)

def teacherdelete( request, iid):
	return serviceTeacher.makeTeacherdelete(request, iid)



###########################################################################

def users(request):
	return render (request, 'store/users.html', locals())

def userManager(request):
    return serviceManager.reportManager(request)
	
