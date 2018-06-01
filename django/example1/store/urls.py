from django.conf.urls import url
from . import views
 
urlpatterns = [
   # url( r'^$',views.index, name ='index'  ),
   url( r'^groups$',views.groups, name ='groups'  ),
   url( r'^group/(?P<iid>\d+)$', views.group, name='group' ),
   url( r'^groupedit/(?P<iid>\d+)$', views.groupedit, name='groupedit'),
   url( r'^groupdelete/(?P<iid>\d+)$', views.groupdelete, name='groupdelete'),
   url( r'^students$',views.students, name ='students'  ),
   url( r'^student/(?P<iid>\d+)$',views.student, name ='student' ),
   url( r'^studentedit/(?P<iid>\d+)$', views.studentedit, name='studentedit'),
]
