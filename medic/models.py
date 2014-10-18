from django.db import models
#from django.core import signals
#from django.utils.translator import ugettext_lazy as _

from datetime import datetime as d_t
#import uuid

class Tmpl(models.Model):
    #id = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % self.name

class Speciality(Tmpl): pass
#models.Model):
#    id = models.CharField(max_length=30)
#    name = models.CharField(max_length=255)

class Patient(Tmpl): pass
#models.Model):
#    id = models.CharField(max_length=10)
#    name = models.CharField(max_length=255)

class Doctor(Tmpl):
#models.Model):
    speciality_id = models.ForeignKey(Speciality)

class Tickets(models.Model):
#    id = models.CharField(max_length=30)
    doctor_id = models.ForeignKey(Doctor)
    date_time = models.DateField(default=d_t.now())
    patient_id = models.ForeignKey(Patient,null=True,blank=True)

    def get_spc_str(self):
        print Doctor.objects.filter(doctor_id=10).select_related('speciality__id', 'name')
        return Doctor.objects.filter(doctor_id=self)

    def __unicode__(self):
        return u'%s' % (self.date_time)

class Repa(models.Model): pass
#    doctor_id = models.ForeignKey(choice=Doctor.bojects.all())
#    date_time = models.DateField(default=d_t.now())
#    patient_id = models.ForeignKey(Patient,null=True,blank=True)
