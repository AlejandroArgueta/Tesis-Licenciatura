#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que calcula el promedio por minuto diurno de todo un año
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
#Leemos el archivo csv
data = pd.read_csv('Fourier Analysis/2017-unam_minuto_L1_cael_filltrend.csv', skiprows=(0,1,2,3,4,5,6))
#Nombramos las columnas
data.columns = ['dates', 'field']
data['dates'] = pd.to_datetime(data['dates'])
data = data.set_index(['dates'])
newdata = data.groupby([data.index.hour, data.index.minute]).mean()
newdata.to_csv('/home/alejandro/MEGA/MEGAsync/Python codes/Fourier Analysis/Meansperminute/meansperminutoUNAM.csv', encoding='utf-8')
