from django import forms

class LoaderForm(forms.Form):
	name = CharField()
	filename = FileField(upload_to=name)

 	def __unicode__(self):
		return u'%s' % self.name
