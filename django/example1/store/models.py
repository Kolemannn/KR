from django.db import models
from datetime import datetime

class Section (models.Model):
    title       = models.CharField ( max_length=255, null=False, blank=False, unique=True )
    teacher     = models.CharField ( max_length=255, null=True)
    datetime    = models.CharField ( max_length=255, null=True)
    level       = models.IntegerField(null=False,default=0)
    # icon
    
    def __str__(self):
        return '{0.title}'.format(self)

class Student (models.Model):
    fioStudent     = models.CharField ( max_length=255, null=False, blank=False )
    faculty        = models.CharField ( max_length=255, null=False, blank=False )
    healthGroup    = models.IntegerField(null=False,default=0)
    sectionStudent = models.ForeignKey ('Section', null = True)

    def __str__(self):
        return '{0.fioStudent}'.format(self)

class Attendance(models.Model):
    date          = models.DateField (null = False)
    attendance    = models.CharField ( max_length=255, null=False, blank=False )
    studentAttend = models.ForeignKey ('Student', null = True)