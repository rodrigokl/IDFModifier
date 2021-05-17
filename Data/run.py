# you would normaly install eppy by doing
# python setup.py install
# or
# pip install eppy
# or
# easy_install eppy

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# if you have not done so, uncomment the following three lines
import sys
# pathnameto_eppy = 'c:/eppy'
pathnameto_eppy = '../'
sys.path.append(pathnameto_eppy)

from eppy.modeleditor import IDF

iddfile = "C:\EnergyPlusV8-3-0\Energy+.idd"
IDF.setiddname(iddfile)

idfname = "C:\Users\Rodrigo\Desktop\IDFModifier\NBR15575_ZB1_VN.idf"
idfname2 = "C:\Users\Rodrigo\Desktop\IDFModifier\NBR15575_ZB1_AC.idf"
lista = [idfname,idfname2]
print lista
epwfile = "C:\EnergyPlusV8-3-0\WeatherData\USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"

j = 0
for i in lista:
	j+=1
	saida = "C:\Users\Rodrigo\Desktop\IDFModifier\%d" %j  
	idf = IDF(i, epwfile)
	idf.run(output_directory=saida)