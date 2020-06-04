import time
import os
#os.chdir('/home/met/Documents/Scripts')
import Master
start = time.time()

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# define the path where the sites folders are stored
path = '/home/alex/Escritorio/MEGAsync/Python codes/Data E Geofisica avg min/'
# define the path where the month data folders are going to be stored
path1 = '/home/alex/Escritorio/MEGAsync/Python codes/Data E Geofisica avg min/'
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*         
# list with the name of the sites
#sites = ['erno', 'jqro','unam']
#sites = ['erno','unam']
sites = ['geof']
# loop for each site
for site in sites:
    print ('*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#')
    print (site)
    # create the folder where the month site data are going to be stored
    L0 = os.path.join(path1,site,'L0') 
    if not os.path.exists(L0):
        os.makedirs(L0)
        os.makedirs(L0 + '/stat')
    # the route of each site folder
    route0 = os.path.join(path,site,'raw')
    # merge the data
    appended_data = Master.merge_files(route0, skip_rows =[0,2,3])
    
    # name of the columns to be extracted
    cols = ['TIMESTAMP','RECORD','E_Avg']
    # print (appended_data.head())
    # appended_data['E_Avg'].update(appended_data['E']) ; del appended_data['E']
    # re-arrange the columns order
   
    appended_data = appended_data[cols]    
    # Avg_frequencies
    appended_data = Master.Avg_frequencies(appended_data)
    # fill_missing_measurements
    appended_data, oldest, youngest = Master.fill_missing_measurements(appended_data.reset_index())
    # get the last data month uploaded 
    # 'site+_RECORD.dat' is file with the record of the upload dates
    Rrd = os.path.join(path,site,'L0',site+'_record.txt')
    # check the record    
    F, R1, FileDate = Master.record(site, Rrd, oldest, youngest)    
    # 'date2' is the string of the first  date to be taken         
    # 'date2' is the string of the last  date to be taken 
    date1 = str(FileDate.strftime('%Y')) + '-' + str(FileDate.strftime('%m'))
    date2 = youngest.strftime('%Y') + '-' + youngest.strftime('%m') + '-' + youngest.strftime('%d')
    # the new 'appended_data' is the range of days contained between data1 & data2
    appended_data = appended_data[date1:date2] 
    # split & save the data by month
    Master.save_month(L0, site, appended_data, extension = '.dat', version = 'L0_cael', MDR = True, sheet_name = 'cael', area = 'Electric field intensity')
    # write the record
    Master.write_record(site, youngest, Rrd, F, R1)
end = time.time()
print ('*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#')
print ('___ Elipsed Time: ' + '%d' % (end - start) + ' s ___')

