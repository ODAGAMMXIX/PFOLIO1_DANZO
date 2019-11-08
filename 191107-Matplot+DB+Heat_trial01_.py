# Import the necessary libraries
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
import pandas as pd
import gmplot
# For improved table display in the notebook
from IPython.display import display
raw_data = pd.read_csv("Addresses_in_the_City_of_Los_Angeles.csv")
# Success! Display the first 5 rows of the dataset
display(raw_data.head(n=5))
display(raw_data.info())

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 998067 entries, 0 to 998066
Data columns (total 18 columns):
HSE_ID            998067 non-null int64
PIN               998067 non-null object
PIND              998067 non-null object
HSE_NBR           998067 non-null int64
HSE_FRAC_NBR      55445 non-null object
HSE_DIR_CD        997408 non-null object
STR_NM            998065 non-null object
STR_SFX_CD        979724 non-null object
STR_SFX_DIR_CD    2175 non-null object
UNIT_RANGE        19424 non-null object
ZIP_CD            998067 non-null int64
LAT               998067 non-null float64
LON               998067 non-null float64
X_COORD_NBR       998067 non-null float64
Y_COORD_NBR       998067 non-null float64
ASGN_STTS_IND     998067 non-null object
ENG_DIST          998000 non-null object
CNCL_DIST         996943 non-null float64
dtypes: float64(5), int64(3), object(10)
memory usage: 137.1+ MB

# Let's limit the dataset to the first 15,000 records for this example
data = raw_data.head(n=15000)

# Store our latitude and longitude
latitudes = data["LAT"]
longitudes = data["LON"]

# Creating the location we would like to initialize the focus on.
# Parameters: Lattitude, Longitude, Zoom
gmap = gmplot.GoogleMapPlotter(34.0522, -118.2437, 10)

# Overlay our datapoints onto the map
gmap.heatmap(latitudes, longitudes)

# Generate the heatmap into an HTML file
gmap.draw("my_heatmap.html")

#############################

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
plt.plot(LON,LAT)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
plt.savefig("C:\\academic-test\\x_y.png")

print('NOW, THE MAP!!')
mapa = folium.Map.render([-23.208, -45.849], zoom_start=11)
LON2=LON.dropna(subset=['LONGITUDE'])
LON2=LAT.dropna(subset=['LATITUDE'])
local = LON2[['LONGITUDE','LATITUDE']].values
#HeatMap(local).add_to(mapa).show
HeatMap(local).add_to(mapa).save(outfile="C:\\academic-test\\heatmap-fucking-hell.png")
mapa

print('TERMINOU!')
r.close()
conn.close()
