# coding: utf-8
anio=input("introduce el año:")
if anio%4==0 and anio%100==0 and anio%400==0:
	print "bisiesto"
else:
	print "no bisiesto"
