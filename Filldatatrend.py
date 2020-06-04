#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que realiza interpolación lineal para datos faltantes
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as md
import numpy as np
#Leemos el archivo csv 
data = pd.read_csv('/home/alex/Escritorio/MEGAsync/Python codes/Fourier Analysis/2018-geof_minuto_L1_cael_filltrend.csv', 
skiprows=(0,1,2,3,4,5,6,7))
data.columns = ['TIMESTAMP', 'field']
data['field'].interpolate(method='linear', inplace=True)
data.to_csv('/home/alex/Escritorio/MEGAsync/Python codes/Fourier Analysis/2018-geof_minuto_L1_cael_filltrend.csv', encoding='utf-8', index=False)  