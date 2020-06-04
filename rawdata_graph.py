#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que grafica los datos crudos de campo eléctrico atmosférico del EFM-100
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as md
#Leemos el archivo efm
data = pd.read_csv('Graphs raw data IGEOF/Data Source 1-04162018.efm')
#Damos nombre a las columnas
data.columns = ['date', 'field', 'v1']
y = data['field']
#Convertimos a datetime la columna de 
#tiempo (que inicialmente solo es object) 
data['date'] = pd.to_datetime(data['date'], format='%H:%M:%S')

fig, ax = plt.subplots(figsize=(10,10))
ax.plot(data['date'], y, color = 'purple')
#Establecemos el formato H:M:S para el eje x
xfmt = md.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)
ax.set_title('Campo eléctrico atmosférico 16-04-2018')
ax.set_xlabel('Hora')
ax.set_ylabel('Campo eléctrico [kV/m]')
plt.grid()
plt.show()


