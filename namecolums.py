#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que les da nombre a las columnas de los datos crudos del Boltek de Geofísica
#Y reemplaza las comillas
import pandas as pd
import csv
data = pd.read_csv('Data E Geofisica avg min/Geof/raw/EFRawAvgMinFebruary2017.csv',)
data.columns = ['TIMESTAMP', 'RECORD', 'E_Avg']
data['TIMESTAMP'] = data['TIMESTAMP'].str.replace('"', '')
print(data.head())
#Sobreescribimos archivo
data.to_csv('Data E Geofisica avg min/Geof/raw/EFRawAvgMinFebruary2017.csv', encoding='utf-8', index=False)    
           