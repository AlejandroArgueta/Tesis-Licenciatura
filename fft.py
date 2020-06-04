#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que realiza la Transformada rápida de Fourier a los datos de campo eléctrico atmosférico
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from scipy import fftpack
from scipy.stats import pearsonr
#Leemos el archivo csv
data = pd.read_csv('Fourier Analysis/2017-jqro_minuto_L1_cael_filltrend.csv', skiprows=(0,1,2,3,4,5,6))
#Nombramos las columnas
data.columns = ['datetime', 'field']
y= data['field']
Y    = np.fft.fft(y)
freq = np.fft.fftfreq(len(y))
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(freq, np.abs(Y), color = 'blue')
ax.set_title('Espectro de Frecuencias Campo eléctrico CCA 2017')
ax.set_xlabel('Frecuencia [Hz]')
plt.grid()
plt.show()
