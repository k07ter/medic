#coding: utf-8

import sys, os
#import psycopg2

def load_data(src):
    src = os.path.realpath(src)
    if os.path.isfile(src):
        with open(src) as f:
            ln = f.readline()
            data = []
            while ln:
                data.append(ln.split(','))
                ln = f.readline()
        return data
    else:
        print u'Проблемы с файлом %s' % src

def cnter():
 	msv = {'dfd': "sdfsdf", "rtg": "egeg", "bgb": "egerg", "fgb": "wqer"}
 	#elm = msv_cnt.next()
 	#while msv_cnt:
	#	yield msv_cnt
	#	#elm = 
	#	msv_cnt.next()

	def ms():
	 	for mi in msv.iteritems():
	 		yield mi
	#while 1:
	for _m in ms(): print _m[0], _m[1]

if __name__ == '__main__':
    #load_data('doctor.txt')
    cnter()
