import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as md
import numpy as np
#Leemos el archivo csv
data = pd.read_csv('Correlations/ECCA04142018raw.csv')
data2 = pd.read_csv('Data E Geofisica avg min/April2018/EFavgmin04142018.csv')
#Damos nombre a las columnas
data.columns = ['TIMESTAMP', 'RECORD', 'field']
data2.columns = ['datetime', 'field']
#Eliminamos comillas
data['TIMESTAMP'] = data['TIMESTAMP'].str.replace('"', '')
#print (data2.head())
y = data['field']
z = data2['field']
#Convertimos a datetime la columna de tiempo (que inicialmente solo es object) 
data['TIMESTAMP'] = pd.to_datetime(data['TIMESTAMP'], format='%Y-%m-%d %H:%M:%S')
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(data['TIMESTAMP'], y, color = 'purple', label="CCA")
ax.plot(data['TIMESTAMP'], z, color = 'red', label="I.Geofísica")
#Pearson Correlation Coefficient
CC = np.corrcoef(y, z)[0,1]
print (CC)
#Establecemos el formato H:M:S para el eje x
xfmt = md.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.set_title('Campo eléctrico atmosférico 26-09-2018')
ax.set_xlabel('Hora')
ax.set_ylabel('Campo eléctrico [kV/m]')
plt.legend()
plt.grid()
plt.show()
