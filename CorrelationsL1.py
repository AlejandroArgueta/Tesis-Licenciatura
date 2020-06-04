#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que grafica en una misma ventana los datos diarios de los Boltek del Instituto de Geofísica
#Y del Centro de Ciencias de la Atmósfera para buscar la correlación entre ellos
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as md
import numpy as np
#Leemos el archivo csv 
data = pd.read_csv('/home/alejandro/MEGA/MEGAsync/Python codes/Correlations/CorrL1/ECCA2018-04-14-L1.csv', skiprows=(0,1,2,3,4,5,6,7))
data2 = pd.read_csv('/home/alejandro/MEGA/MEGAsync/Python codes/Correlations/CorrL1/Egeof2018-04-14-L1.csv', skiprows=(0,1,2,3,4,5,6,7))
#Damos nombre a las columnas
data.columns = ['TIMESTAMP', 'field']
data2.columns = ['TIMESTAMP', 'field']
#print (data2.head())
y = data['field']
z = data2['field']
#Convertimos a datetime la columna de tiempo (que inicialmente solo es object) 
data['TIMESTAMP'] = pd.to_datetime(data['TIMESTAMP'], format='%Y-%m-%d %H:%M:%S')
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(data['TIMESTAMP'], y, color = 'purple', label="CCA")
ax.plot(data['TIMESTAMP'], z, color = 'red', label="I.Geofísica")
#Establecemos el formato H:M:S para el eje x
xfmt = md.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.text(0.95, 0.01, 'r=0.465',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=25)
ax.set_title('Campo eléctrico atmosférico 14-04-2018')
ax.set_xlabel('Hora')
ax.set_ylabel('Campo eléctrico [kV/m]')
plt.legend()
plt.grid()
plt.show()
