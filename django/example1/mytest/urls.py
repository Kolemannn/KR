from django.conf.urls import url
from . import views
 
urlpatterns = [
    url( r'^$',views.index, name ='index'  ),
    url( r'^time$',views.curtime, name ='curtime'  ),
    url( r'^people$',views.people, name ='people'  ),
]
