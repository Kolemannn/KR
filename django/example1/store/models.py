from django.db import models
from datetime import datetime



class Teacher (models.Model):
    fioTeacher     = models.CharField ( max_length=255, null=False, blank=False )
    sport          = models.CharField ( max_length=255, null=False, blank=False )
    contTeacher    = models.CharField ( max_length=255, null=False, blank=False )
    trackRecord    = models.CharField ( max_length=255, null=False, blank=False )
    grade          = models.IntegerField (null=False,default=0)

    def __str__(self):
        return '{0.fioTeacher}'.format(self)


class Section (models.Model):
    title       = models.CharField ( max_length=255, null=False, blank=False )
    teacher     = models.ForeignKey ('Teacher', null = True)
    datetime    = models.CharField ( max_length=255, null=True)
    level       = models.IntegerField(null=False,default=0)

    
    def __str__(self):
        return '{0.title}'.format(self)

class Student (models.Model):
    fioStudent     = models.CharField ( max_length=255, null=False, blank=False )
    faculty        = models.CharField ( max_length=255, null=False, blank=False )
    healthGroup    = models.IntegerField(null=False,default=0)
    sectionStudent = models.ForeignKey ('Section', null = True)
    contStudent       = models.CharField ( max_length=255, null=False, blank=False )
    
    def __str__(self):
        return '{0.fioStudent}'.format(self)


class Attendance(models.Model):
    date          = models.DateField (null = False)
    attendance    = models.BooleanField ( null=False, blank=False )
    studentAttend = models.ForeignKey ('Student', null = True)
    reason        = models.CharField (max_length=255, default='Укажите причину')

    def __str__(self):
        return '{0.attendance}'.format(self)

