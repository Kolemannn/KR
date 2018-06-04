from django.conf.urls import url
from . import views
 
urlpatterns = [
   # url( r'^$',views.index, name ='index'  ),

   url( r'^groups$',views.groups, name ='groups'  ),
   url( r'^group/(?P<iid>\d+)$', views.group, name='group' ),
   url( r'^groupedit/(?P<iid>\d+)$', views.groupedit, name='groupedit'),
   url( r'^groupdelete/(?P<iid>\d+)$', views.groupdelete, name='groupdelete'),
   url( r'^groupcreate/$', views.groupcreate, name='groupcreate' ),
   
   url( r'^students$',views.students, name ='students'  ),
   url( r'^student/(?P<iid>\d+)$',views.student, name ='student' ),
   url( r'^studentedit/(?P<iid>\d+)$', views.studentedit, name='studentedit'),
   
   url( r'^teachers$', views.teachers, name='teachers'),
   url( r'^teacher/(?P<iid>\d+)$', views.teacher, name='teacher' ),
   url( r'^teachercreate/$', views.teachercreate, name='teachercreate' ),
   url( r'^teacheredit/(?P<iid>\d+)$', views.teacheredit, name='teacheredit'),
   url( r'^teacherdelete/(?P<iid>\d+)$', views.teacherdelete, name='teacherdelete'),

   url( r'^users/$', views.users, name='users' ),
   url( r'^userManager/$',views.userManager, name ='userManager' )
]
