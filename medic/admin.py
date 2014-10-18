from models import Patient, Speciality, Doctor, Tickets
from django.contrib import admin

class PatientAdmin(admin.ModelAdmin): pass
class SpecialityAdmin(admin.ModelAdmin): pass
class DoctorAdmin(admin.ModelAdmin): pass

class TicketAdmin(admin.ModelAdmin):
    class Meta:
        order = ('id',)

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Tickets, TicketAdmin)
