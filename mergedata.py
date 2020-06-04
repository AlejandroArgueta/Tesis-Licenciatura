#UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
#Argueta Hernández, Fidel Alejandro alejo_tigres@yahoo.com
#Programa que une datos diarios de campo eléctrico promediados
#Y les da el formato crudo de los dataloggers de la RUOA
import pandas as pd
import shutil
#Creamos nuevo archivo mensual a partir de datos diarios
#with open('Data E Geofisica avg min/EFRawAvgMw.csv','wb') as wfd:
with open('/home/alejandro/MEGA/MEGAsync/Python codes/Fourier Analysis/2017-jqro_minuto_L1_cael.csv','wb') as wfd:
    for f in ([
    #     'Data E Geofisica avg miw/EFavgmin06012019.csv',
    # 'Data E Geofisica avg miw/EFavgmin06022019.csv',
    # 'Data E Geofisica avg miw/EFavgmin06032019.csv',
    # 'Data E Geofisica avg miw/EFavgmin06042019.csv',
    # 'Data E Geofisica avg miw/EFavgmin06052019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05062019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05072019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05082019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05092019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05102019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05112019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05122019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05132019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05142019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05152019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05162019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05172019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05182019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05192019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05202019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05212019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05222019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05232019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05242019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05252019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05262019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05272019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05282019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05292019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05302019.csv',
    # 'Data E Geofisica avg miw/EFavgmin05312019.csv',
    #Con lo siguiente vamos a unir los archivos de 2018
    'Data L1/Juriquilla/2017-01-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-02-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-03-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-04-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-05-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-06-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-07-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-08-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-09-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-10-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-11-jqro_minuto_L1_cael.csv',
    'Data L1/Juriquilla/2017-12-jqro_minuto_L1_cael.csv']):
        with open(f,'rb') as fd:
            shutil.copyfileobj(fd, wfd)
            #Abrimos archivo recién creado para darle formato
            #data = pd.read_csv('/Fourier Analysis/2018-geof_minuto_l1_cael.csv')
# data.columns = ['datetime', 'field'] #Damos nombres a las columnas
# #data['datetime'] = '"' + data['datetime'] + '"' #Ponemos comillas al datetime
# data['index'] = data.index #Creamos índice
# data = data[['datetime', 'index', 'field']] #Reorganizamos columnas
# print(data) #Imprimimos datos para visualizar correcto funcionamiento
# #Sobreescribimos archivo
# data.to_csv('Data E Geofisica avg min/EFRawAvgMw.csv', encoding='utf-8', index=False)    
           


