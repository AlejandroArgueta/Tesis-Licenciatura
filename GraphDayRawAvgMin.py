#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que grafica datos crudos de un día promediados por minuto 
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as md
#Leemos el archivo efm
data = pd.read_csv('Data E Geofisica avg min/May2019/EFavgmin05202019.csv')
#Damos nombre a las columnas
data.columns = ['datetime', 'field']
y = data['field']
#Convertimos a datetime la columna de tiempo (que inicialmente solo es object) 
data['datetime'] = pd.to_datetime(data['datetime'], format='%Y-%m-%d %H:%M:%S')

fig, ax = plt.subplots(figsize=(10,10))
ax.plot(data['datetime'], y, color = 'purple')
#Establecemos el formato H:M:S para el eje x
xfmt = md.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.set_title('Campo eléctrico atmosférico 19-05-2018')
ax.set_xlabel('Hora')
ax.set_ylabel('Campo eléctrico [kV/m]')
plt.grid()
plt.show()
