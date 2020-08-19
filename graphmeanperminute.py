#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que calcula el promedio por minuto diurno de todo un año
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.dates as md
import matplotlib.ticker as plticker
data = pd.read_csv('/home/alejandro/MEGA/MEGAsync/Python codes/Fourier Analysis/Meansperminute/meansperminuteUNAM.csv', skiprows=0)
data.columns = ['hour', 'minute', 'field', 'points', 'datetime']
x = data['datetime']
z = data['field']
x = pd.to_datetime(data['datetime'], format='%H:%M')
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(x,z, color = 'purple')
xfmt = md.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.set_title('Promedio diurno del campo eléctrico atmosférico para 2017 en el CCA')
ax.set_xlabel('Hora') 
ax.set_ylabel('Campo eléctrico [kV/m]') 
plt.grid()
plt.show()