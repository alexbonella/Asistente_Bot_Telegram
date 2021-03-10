"""

*********************************************************************** 
Autor = @lexbonella                                                   *  
Fecha = '06/03/2021'                                                  * 
Nombre = Web Scrapping resultados de loteria                          *
Descripción : Bot que envia los resultados de loteria a un usuario    * 
*********************************************************************** 

"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os 
from tqdm import tqdm
import time
import random
import webbrowser



"""Leemos los datos de nuestra webiste"""
df=pd.read_html('https://resultadodelaloteria.com/colombia/') # Lectura del webiste

"""Loterias que jugaron el dia anterior"""
lot_ant=df[1]
lot_ant=lot_ant.rename(columns={0:'Loteria'})
lot_ant=lot_ant.drop(index=[0],axis=1)
lot_ant=lot_ant.reset_index(inplace=False)
lot_ant=lot_ant.drop(columns='index')

"""Leemos archivo con las Url's de todas las loterias"""
df_lot=pd.read_csv('Loterias_link.csv')
df_lot=df_lot.drop(columns='Unnamed: 0')

"""Merge para rescatar los links de las loterias"""
df_final=pd.merge(df_lot,lot_ant,how='inner',on='Loteria')


"""Extraemos los resultados de todas las loterias"""
last_day=[]
loteria=[]
for i in tqdm(range(len(df_final['url']))):

    try : 
        a=pd.read_html(df_final['url'][i])
        temp=pd.DataFrame(a[1].loc[0])
        last_day.append(temp.T)
        loteria.append(df_final['Loteria'][i])
        time.sleep(random.randint(1,3))
    except : 
        pass

# Creación del Dataframe final
dia_anterior=pd.concat(last_day,ignore_index=True)
dia_anterior['Loteria']=loteria


"""Establecemos correccíon de ceros para 3 y 4 cifras"""
df_file=dia_anterior
df_file.loc[df_file['Loteria']=='Cash Three Día','Cifras']=3
df_file.loc[df_file['Loteria']=='Cash Three Noche','Cifras']=3
df_file.loc[(df_file['Loteria']!='Cash Three Noche') & (df_file['Loteria']!='Cash Three Día'),'Cifras']=4
df_file['Cifras']=df_file['Cifras'].apply(lambda x : int(x))
df_file['Resultado']=df_file['Resultado'].apply(lambda x : str(x))

"""Limpieza de resultados """
for i in tqdm(range(len(df_file))): 
        
    try : 
        df_file['Resultado'][i]=df_file['Resultado'][i].split('serie')[0].strip()
    except: 
        pass


for i in tqdm(range(len(df_file))):
    
    if (df_file['Cifras'][i]==4) & (len(df_file['Resultado'][i])==3):

        df_file['Resultado'][i]='0'+str(df_file['Resultado'][i])

    elif (df_file['Cifras'][0]==4) & (len(df_file['Resultado'][i])==2):

        df_file['Resultado'][i]='00'+str(df_file['Resultado'][i])

    elif (df_file['Cifras'][i]==4) & (len(df_file['Resultado'][i])==1):

        df_file['Resultado'][i]='000'+str(df_file['Resultado'][i])

    elif (df_file['Cifras'][i]==3) & (len(df_file['Resultado'][i])==2):

        df_file['Resultado'][i]='00'+str(df_file['Resultado'][i])

    elif (df_file['Cifras'][i]==3) & (len(df_file['Resultado'][i])==1):

        df_file['Resultado'][i]='00'+str(df_file['Resultado'][i])

    elif (df_file['Cifras'][i]==3) & (len(df_file['Resultado'][i])<1):

        df_file['Resultado'][i]='000'

    elif (df_file['Cifras'][i]==3) & (len(df_file['Resultado'][i])<1):

        df_file['Resultado'][i]='0000'
        
historico=[]
for i in tqdm(range(len(df_file))):
    historico.append({
        'Loteria': df_file['Loteria'][i],
        'Resultado':str(df_file['Resultado'][i]),
        'Fecha':df_file['Fecha'][i],
        'Sorteo N°':str(df_file['# Sorteo'][i])
})
    
"""Creamos nuestro archivo csv"""
df_file=pd.DataFrame(historico)
df_file=df_file.drop(columns=['Fecha','Sorteo N°'])
df_file.set_index('Loteria', inplace=True)
        
"""Impresión de todos los resultados """

print('\n RESULTADOS CARGADOS EXITOSAMENTE \n')

