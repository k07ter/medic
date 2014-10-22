from django.db import models

from datetime import datetime as d_t

class Tmpl(models.Model):
    name = models.CharField(max_length=255)

    def get_inf(self, oid=None):
	so = self.objects
 	if oid:
		return so.filter(pk=oid)
 	else:
		return so.all()

    def __unicode__(self):
        return u'%s' % self.name

class Speciality(Tmpl): pass
#    def get(self, dct_id):
# 	return Doctor.objects.all()

class Patient(Tmpl): pass

class Doctor(Tmpl):
    speciality_id = models.ForeignKey(Speciality)

    def get_prof(self):
 	return '111' #Speciality.objects.all().values() #get(speciality_id=prof_id)

    def cut_by_ptn(self, name=None):
	return Tickets.objects.values('doctor_id').annotate(ptn_cnt=Count('patient_id'))

class Tickets(models.Model):
    doctor_id = models.ForeignKey(Doctor)
    date_time = models.DateField(default=d_t.now())
    patient_id = models.ForeignKey(Patient,null=True,blank=True)

    def get_doc(self):
        return Doctor.objects.all().values()

    def get_ptn(self, doc_id=None):
 	return Patient.objects.all()

    def get_visited(self, doc_id=None):
 	return Tickets.objects.filter(models.Q(patient_id__isnull=false)).values('doctor_id').annotate(ptn_cnt=models.Count('patint_id'))

    def __unicode__(self):
        return u'%s' % (self.date_time)
