import pandas as pd
import sqlite3
import os
import io
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
from datetime import datetime
import folium
from folium import plugins
from folium.plugins import HeatMap

with sqlite3.connect("C:\\academic-test\\191016-G-danzodb.db") as con:
    sql = '''
        SELECT LONGITUDE
          FROM \'DadosBO_2019_8(FURTO_VEÍCULO)\'
          GROUP BY LONGITUDE
    '''

    sql = 'SELECT LATITUDE FROM \'DadosBO_2019_8(FURTO_VEÍCULO)\' ORDER BY LONGITUDE ASC'
    table = pd.read_sql(sql, con)['LATITUDE','LONGITUDE']
    print(table)
    #table = table.reindex(index=order, columns=order)
    #table = df.pivot(index=None, columns='LONGITUDE', values=None)
    #mapa = folium.Map([-23.208, -45.849], zoom_start=11)
    #local = df.table[['LATITUDE', 'LONGITUDE']].values
    #HeatMap(local).add_to(mapa)
    #mapa

#from IPython.display import Image
#Image("HeatMapSJC.png", width=950, height=850)
