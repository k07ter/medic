#coding: utf-8
import unittest
import doctest
DJANGO_SETTINGS_MODULE = 'settings'
from django import test
from models import Doctor

class DoctorTestCase(unittest.TestCase):
 	""" Покрытие тестами методов класса: get_dct_name, get_spc
	"""
	def __init__(self):
		print dir(self)
 		print dir(Doctor)

 	def setUp(self):
 	 	return 1 #Doctor.objects.get(name=name)

 	def testDoctorSum(self):
 	 	""" Blank"""
 	 	test_sum = 120
		op = 20
 	 	#self.dct = Doctor('Иванов Иван Иваныч')
 	 	self.assertEqual(100+op,test_sum)

def main():
	dct = DoctorTestCase()
 	dct.testDoctorSum()
	unittest.main() #Suite(DoctorTestCase)

if __name__ == '__main__':
	main()
