import pandas as pd
import sqlite3
import time
import os
import io
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
from datetime import datetime
import folium
from folium import plugins
from folium.plugins import HeatMap

conn = None
try:
    conn = sqlite3.connect("C:\\academic-test\\191016-G-danzodb.db")
    print(conn)
except Error as e:
    print(e)
r = conn.cursor()
df = pd.read_sql_query("select * from 'DadosBO_2019_8(FURTO_VEÍCULO)'", conn)
print(df)
#time.sleep(2)
#plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])
#list comprehension (rotina p/ conversão de TXT p/ NUM)
LON = pd.read_sql_query("select LONGITUDE from 'DadosBO_2019_8(FURTO_VEÍCULO)'", conn)
LAT = pd.read_sql_query("select LATITUDE from 'DadosBO_2019_8(FURTO_VEÍCULO)'", conn)
plt.plot(LON, LAT)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
plt.savefig('x_y.png')

mapa = folium.Map([-23.208, -45.849], zoom_start=11)
LON2=LON.dropna(subset=['LONGITUDE'])
LON2=LAT.dropna(subset=['LATITUDE'])
local = LON2[['LATITUDE', 'LONGITUDE']].values
HeatMap(local).add_to(mapa)
mapa

print('TERMINOU!')
r.close()
conn.close()

