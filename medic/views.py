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
 	if type(menu) == 'dict':
 	 	self.menu = menu.keys()
		 #)||menu.keys()
 	 	self.items = menu.values()
 	 	self.compil()
 	else: return

    def compil(self):
 	print self.menu
 	while 1:
 	 	print self.items
 	 	yield self.items
 	 	break

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
    tip = req.META['PATH_INFO'].split('/')[1]
    baza = eval(LINKS[tip][0]).objects.all()
    return render_to_response('%s.html' % trg, {'data': tip, 'store': baza})

def doctor(request):
    page = 'monitor'
    #tip = 'doctor'
    #baza = Doctor.objects.all()
    #print baza
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
    baza = 'Doctor' #.objects.all()
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
    #for b in baza3.all().values():
    #    print b #['id'], b['name']
    #for b in baza4.all().values():
    #    print b #['id'], b['name']

    #load_data(os.path.realpath('doctor.txt'))
    for ln in load_data('%s.txt' % base_lst[2]):
            #if baza.filter(name=ln[0]):
            #lst = baza.filter(name=u'%s' % ln[0]).values_list()
            #for l in lst:
        #print ln[0], ln[1], ln[2], ln[3]
        #baza4.filter(id=int(ln[0])).update(doctor_id=int(ln[1])+9)
        #baza4.create(name=ln[0], speciality_id_id=int(ln[1]))
        # baza4.create(doctor_id_id=int(ln[1]),
        #              date_time=datetime.strptime(ln[2],
        #                                         '%Y-%m-%d %H:%M:%S'))

        #print dir(baza4)
        #print dir(ln[3])
        #print baza4.filter(doctor_id_id=int(ln[1])).values() #.update(id=int(ln[1])+3)
        #baza4.save()
        if ln[3].strip() != 'null':
            print ln[3]
            #baza4.filter(id=int(ln[0])).update(patient_id=int(ln[3])+4)
            #baza4.save()
            #print ln[0], ln[1], ln[2], ln[3]
            #baza4.create(doctor_id_id=int(ln[0])+3),
            #conv = datetime.strftime(now,'%d-%m-%Y %H:%M:%S')
            #baza4.update(date_time=datetime.strftime(ln[2],
            #                                         '%Y-%m-%d %H:%M:%S'))
        #else:
            #baza4.create(doctor_id_id=int(ln[0])+3,
            #             date_time=datetime.strptime(ln[2],
            #                                         '%Y-%m-%d %H:%M:%S').__str__,
            #baza4.filter(doctor).update(patient_id_id=int(ln[3]))
            #baza4.filter(doctor_id_id=int(ln[1]),id=int(ln[1])).update(patient_id=int(ln[3])+7)
            #    .values()
        #else:
        #    print u'Пусто' #ln[2]
    #print baza4.all().values() #filter(doctor_id_id>0).values()
    #print dir(baza)
    #baza.filter(name=u'Педиатр').update(id=3)
        #baza.create(name=inf[0], speciality_id=int(inf[1]))
    #baza.save()
    #    if request.method == 'POST':
    #        uform = ReportProfForm(data=request.POST)
    #        pform = UserProfForm(data=request.POST)
    #    if uform.is_valid():
    #        user.uform.save()
        #print ln[0]
    #    Doctor.objects.all()
    return render_to_response('%s.html' % page, {'data': tip, 'store': ['baza']})

def rep_comm(request):
    from django.db.models import Count, Sum
    #print Menu(LINKS)
    page = 'report'
    tck = Tickets.objects
 	
    # Все пришедшие пациенты
    _data = tck.filter(Q(patient_id__isnull=False))
    _t = tck.values('doctor_id').annotate(ptn_cnt=Count('patient_id'))

    #TODO: Получить словарь с количетвом посещений и талонов для каждого врача
    _rpt = _t.annotate(tck_cnt=Count('doctor_id'))
    #_rpt = _rpt.annotate(ptn_cnt=Count('patient_id')) #.values() #'doctor_id', 'ptn_cnt')
    #print Tickets.objects.get(doctor_id=11)
    print _rpt.values('doctor_id','tck_cnt','ptn_cnt')
    #print _rpt.values('doctor_id','tck_cnt','tck_cnt')
    _data_r = []
    _data_rpt = {}
    _spc = Speciality.objects
    _spc2 = Speciality.objects.all()
    _doc = Doctor.objects
    _cond = _spc2.values()
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
                    #_data_rpt[_sp].append(tck.filter(doctor_id__in=doct).values("doctor_id","patient_id").count())
    #stat2 = [''] #tck.values("patient_id").annotate(cnt2=Count('patient_id')).order_by()
    return render_to_response('%s.html' % page,
                              {'req_data': _data_rpt,
                               'req_lst': _data,
                               'req_cond': _cond,
                               'ss': _spc2, 'dd': _doc,
                               'tt': tck,'rslt': _rpt},
                               context_instance=RequestContext(request))

def test(request):
 	return render_to_response('page.html')
