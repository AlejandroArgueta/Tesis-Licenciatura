#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que crea una gráfica de calidad L2 de los datos por estación a partir de un CSV
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as md
#Leemos el archivo csv
data = pd.read_csv('L2 analysis/Juriquilla/L2/graficacalidadjqro.csv')
#Nombramos las columnas
data.columns = ['datetime', 'escala1', 'escala2', 'escala3', 'escala4']
v= data['escala1']
w= data['escala2']
y= data['escala3']
z= data['escala4']
#Convertimos a datetime la columna de tiempo (que inicialmente solo es object) 
x = pd.to_datetime(data['datetime'], format='%Y-%m-%d')

fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(x, w, color = 'green', label='Calidad alta')
ax.scatter(x, y, color = 'yellow', label='Calidad media')
ax.scatter(x, z, color = 'red', label='Calidad baja')
ax.scatter(x, v, color = 'gray', label='Sin datos')
#Establecemos el formato de días y luego H:M:S para el eje x
xfmt = md.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(xfmt)
ax.set_title('Calidad datos campo eléctrico atmosférico Juriquilla')
ax.set_xlabel('Año-mes-día')
ax.set_ylabel('Escala arbitraria del 0 al 10')
plt.legend(loc='upper right', bbox_to_anchor=(1, 0.9))
plt.grid()
plt.show()