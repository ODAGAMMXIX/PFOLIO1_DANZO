import pandas as pd
import sqlite3
import os
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
#conn = str()
#r = conn.cursor()
#(r.execute('select * from "DadosBO_2019_8(FURTO DE VEÍCULO"'))
#results = r.fetchall()
#print(r)
df = pd.read_sql_query("select LATITUDE from 'DadosBO_2019_8(FURTO DE VEÍCULO'", conn)
print(df)
#time.sleep(2)

mapa = folium.Map([-23.208, -45.849], zoom_start=11)
r.dropna(subset=pd.read_sql_query['LATITUDE'])
r.dropna(subset=pd.read_sql_query['LONGITUDE'])
local = r[['LATITUDE', 'LONGITUDE']].values
HeatMap(local).add_to(mapa)
mapa

r.close()
conn.close()
