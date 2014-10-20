from django import forms

class DoctorForm(forms.Form):
 	name = forms.CharField(label='Доктор')

class PatientForm(forms.Form):
 	name = forms.CharField(label='Пациент')
