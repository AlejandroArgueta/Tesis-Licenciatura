#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que grafica la varianza diurna del campo eléctrico
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.dates as md
import matplotlib.ticker as plticker
data = pd.read_csv('/home/alejandro/MEGA/MEGAsync/Python codes/Fourier Analysis/varianza/varianzaJQROgraph.csv', skiprows=0)
data.columns = ['hora', 'promedio', 'varianza']
x = data['hora']
y = data['varianza']
x = pd.to_datetime(data['hora'], format='%H:%M')
fig, ax = plt.subplots(figsize=(10,10))
ax.bar(x,y, color = 'purple', width=0.05)
xfmt = md.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
ax.set_title('Varianza diurna del campo eléctrico atmosférico promedio para 2017 en Juriquilla')
ax.set_xlabel('Hora') 
ax.set_ylabel('Varianza [kV/m]^2') 
plt.grid()
plt.show()