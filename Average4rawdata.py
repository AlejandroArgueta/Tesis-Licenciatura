#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que saca promedio por minuto de los datos crudos 
# de campo eléctrico
import pandas as pd
data = pd.read_csv('Graphs raw data IGEOF/Data Source 1-06052019.efm') 
#Leemos el archivo efm. If wrong won't run
data.columns = ['time', 'field','v1'] #Damos nombre a las columnas
data['dates'] = "2019-06-05" #Creamos columna con fecha del día. 
If wrong we'll see in terminal 
data['datetime'] = data['dates'] + ' ' + data['time'] #Sumamos 
columnas de fecha y de hora
data=data[['datetime','field']] #Nos quedamos con las columnas que nos interesan
data['datetime'] = pd.to_datetime(data['datetime'], 
format='%Y-%m-%d %H:%M:%S') 
#Covertimos a formato datetime
data = data.set_index(data['datetime']) #Trasladamos a Index columna datetime
data=data['field'].resample('1Min').mean() #Promediamos 
por minuto
print(data.head()) #Imprimimos para verificar correcto 
#funcionamiento
#Creamos nuevo archvivo. If wrong, merge won't work
data.to_csv('Data E Geofisica avg min/June2019/EFavgmin06052019.csv', 
encoding='utf-8', header=False) 

