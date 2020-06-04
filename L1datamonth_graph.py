#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que grafica los datos procesados L1 de campo eléctrico atmosférico del EFM-100
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as md
#Leemos el archivo csv
#data = pd.read_csv('L2 analysis/CCA/2017-01-unam_minuto_L1_cael.csv', skiprows=(0,1,2,3,4,5,6))
#Para graficar año
data = pd.read_csv('Fourier Analysis/2017-unam_minuto_L1_cael_filltrend.csv', skiprows=(0,1,2,3,4,5,6))
#Nombramos las columnas
data.columns = ['datetime', 'field']
y= data['field']
#Convertimos a datetime la columna de tiempo (que inicialmente solo es object) 
x = pd.to_datetime(data['datetime'], format='%Y-%m-%d %H:%M:%S')

fig, ax = plt.subplots(figsize=(10,10))
ax.plot(x, y, color = 'purple')
#Establecemos el formato de días y luego H:M:S para el eje x
#xfmt = md.DateFormatter('%d %H:%M')
#Establecemos el formato de mes-día para cuando graficamos año
xfmt = md.DateFormatter('%m-%d')
ax.xaxis.set_major_formatter(xfmt)
ax.set_title('Campo eléctrico atmosférico CCA 2017')
#Título eje x cuando graficamos por mes
#ax.set_xlabel('Día Hora:Minuto')
#Título eje x cuando graficamo año
ax.set_xlabel('Mes-Día')
ax.set_ylabel('Campo eléctrico [kV/m]')
plt.grid()
plt.show()