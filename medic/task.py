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

if __name__ == '__main__':
    load_data('doctor.txt')