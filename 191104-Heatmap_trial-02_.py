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
#def make_table(filename):
    # make sqlite table
#with sqlite3.connect("C:\\academic-test\\191016-G-danzodb.db") as con:
 #       df = pd.read_table(io.BytesIO(text), sep=r'\s*[|]\s*').iloc[:, 1:-1]
 #       df.to_sql('dataset', con=con, if_exists='replace')

#filename = '/tmp/data.sqlite'
#make_table(filename)

with sqlite3.connect("C:\\academic-test\\191016-G-danzodb.db") as con:
    sql = '''
        SELECT LONGITUDE
          FROM \'DadosBO_2019_8(FURTO_VEÍCULO)\'
          GROUP BY LONGITUDE
    '''
    df = pd.read_sql(sql, con)
    table = df.pivot(index=None, columns='LONGITUDE', values=None)
    print (table)

    sql = 'SELECT LATITUDE FROM \'DadosBO_2019_8(FURTO_VEÍCULO)\' ORDER BY BO_EMITIDO ASC'
    order = pd.read_sql(sql, con)['LATITUDE']
    table = table.reindex(index=order, columns=order)

    fig, ax = plt.subplots()
    ax.pcolor(table.values, cmap=plt.get_cmap('jet'),
              vmin=df['min_value'].min(), vmax=df['min_value'].max())
    ax.set_xticks(np.arange(table.shape[1] + 1)+0.5, minor=False)
    ax.set_xticklabels(table.columns, minor=False)
    ax.set_yticks(np.arange(table.shape[0] + 1)+0.5, minor=False)
    ax.set_yticklabels(table.index, minor=False)
    ax.set_xlim(0, table.shape[1])
    ax.set_ylim(0, table.shape[0])
    plt.show()
