#coding: utf-8

from django.shortcuts import render_to_response
from django.db.models import Q
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from models import Speciality, Patient, Doctor, Tickets

LINKS = {
    'speciality': ('Speciality','Специальности'),
    'patients': ('Patient','Пациенты'),
    'doctor': ('Doctor','Врачи'),
    'tickets': ('Ticket','Талончики'),
    'report': (' ','Отчет'),
}
#,[2,0,1,3,4]]

class Menu:
    def __init__(self, menu):
 	self.out = render_to_response('%s.html' % 'page', {'links': LINKS})
 	self.menu = menu.keys()
	if self.menu:
 	 	for itm in self.compil():
 	 		print itm #, menu[itm]
    #def item(self, name):
    #	return name

    def compil(self):
 	self.items = (v for v in menu.values())
 	for i in self.items:
 	 	yield i

def one_page(request):
    paginator = Paginator(list, 10)
    try: 
        page= int(request.GET.get('page','1'))
    except ValueError:
        page=1
    try:
        p_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        p_list = paginator.page(paginator.num_pages)

def home(request):
    mnu = Menu(LINKS)
    return render_to_response('%s.html' % 'page', {'links': LINKS})

def output(request):
    return render_to_response('%s.html' % 'page', {'links': LINKS})

def outp():
    def answer(*args, **kwargs):
        #req = request.META['PATH_INFO']
        #print request.META
        #cmd(*args, **kwargs)
        #print args
        #print kwargs
        return True
    return answer

#@outp()
def prep(req, trg):
    tip = req.META.get('PATH_INFO', None)
    if tip: tip = tip.split('/')[1]
    baza = eval(LINKS[tip][0]).objects.all()
    return render_to_response('%s.html' % trg, {'data': tip, 'store': baza})

def doctor(request):
    page = 'monitor'
    return prep(request, page)
    #return render_to_response('%s.html' % page, {'data': tip, 'store': baza})

def patients(request):
    page = 'monitor'
    tip = 'patient'
    baza = Patient.objects.all()
    #print baza
    return render_to_response('%s.html' % page, {'data': tip, 'store': baza})

def tickets(request):
    page = 'monitor'
    tip = 'doctor'
    baza = 'Doctor'
    #.objects.all()
    #print baza
    return render_to_response('%s.html' % page, {'data': tip, 'store': ['baza']})

def new_doctor(request):
    import os
    from task import load_data
    from datetime import datetime
    now = datetime.now()
    #print dir(now)
    #conv = datetime.strftime(now,'%d-%m-%Y %H:%M:%S')
    page = 'monitor'
    tip = 'doctor'
    baza = Doctor.objects
    baza2 = Speciality.objects
    baza3 = Patient.objects
    baza4 = Tickets.objects

    base_lst = ['doctor', 'patients','tickets','speciality']

    for ln in load_data('%s.txt' % base_lst[2]):
        if ln[3].strip() != 'null':
            print ln[3]
    return render_to_response('%s.html' % page, {'data': tip, 'store': ['baza']})

def rep_comm(request):
    from django.db.models import Count, Sum
    #print Menu(LINKS)
    page = 'report'
    tck = Tickets.objects
 	
    # Все пришедшие пациенты
    _data = tck.filter(Q(patient_id__isnull=False))
    _t = _data.values('doctor_id').annotate(ptn_cnt=Count('patient_id'))

    #TODO: Получить словарь с количетвом посещений и талонов для каждого врача
    _rpt = _t.annotate(tck_cnt=Count('doctor_id'))
    _data_r = []
    _data_rpt = {}
    _spc = Speciality.objects
    _spc2 = Speciality.objects.all()
    _cond = _spc2.values()
    _doc = Doctor.objects
    talony = tck.values('doctor_id__speciality_id__tmpl_ptr__id')#,'doctor_id','patient_id')
    tck_done = talony.annotate(vst=Count('patient_id'))
    tck_done = tck_done.annotate(vse=Count('doctor_id__speciality_id__tmpl_ptr__id'))
    t_rep = tck_done
    t_comm = tck_done.values('doctor_id','vse','vst')
    t_ind = tck.filter().values('doctor_id').annotate(ind=Count('patient_id'))
    t_comm = t_ind.values('doctor_id','ind')

    for _s in _cond:
        _dr = _doc.filter(speciality_id_id=_s['tmpl_ptr_id'])
 	#.values() #'tmpl_ptr_id') #,'name')#.get('speciality_id')
        if _dr.values():
            _sp = _s['name']
            _data_rpt[_sp] = [_dr.values('id')]
            for _c in _rpt:
                doct = map(lambda x: x[0],_dr.values_list('tmpl_ptr_id'))
                if _c.get('doctor_id') in doct:
                    _data_rpt[_sp].append(_data.filter(doctor_id__in=doct).values("doctor_id","patient_id").count())
    return render_to_response('%s.html' % page,
                              {'req_data': _data_rpt,
                               'req_lst': _data,
                               'req_cond': _cond,
                               'ss': _spc2, 'dd': _doc,
                               'tt': tck,'rslt': _rpt, 'TktRep': t_rep, 'TktComm': t_comm},
                               context_instance=RequestContext(request))

def test(request):
 	return render_to_response('page.html')
