#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que grafica datos crudos de un mes promediados por minuto 
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as md
data = pd.read_csv('Data E Geofisica avg min/Geof/raw/EFRawAvgMinJuly2017.csv', skiprows=[0,2,3])
y = data['E_Avg']
data['TIMESTAMP'] = pd.to_datetime(data['TIMESTAMP'], format='%Y-%m-%d %H:%M:%S')
print(data.head())
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(data['TIMESTAMP'], y, color = 'purple')
xfmt = md.DateFormatter('%d %H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.set_title('Campo eléctrico atmosférico Julio 2017')
ax.set_xlabel('Día Hora:Minuto')
ax.set_ylabel('Campo eléctrico [kV/m]')
plt.grid()
plt.show()
