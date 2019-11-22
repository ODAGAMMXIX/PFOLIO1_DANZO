import io
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.pyplot.savefig(fname=olhaissomano, dpi=None, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1,frameon=None, metadata=None)

plt.plot(range(10))
plt.savefig('testplot.png')
Image.open('testplot.png').save('testplot.jpg','JPEG')

import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with the 'png' Renderer"
)
fig.show()

text = '''\
| ID | SourceID | TargetID | Parameter | Values  |
| 1  |    21    |    34    | 23.46513  | 0.12654 |
| 2  |    21    |    34    | 23.46513  | 0.25478 |
| 3  |    21    |    46    | 23.46513  | 0.43564 |
| 4  |    21    |    46    | 23.46513  | 1.02487 |
| 5  |    34    |    21    | 14.56319  | 0.01476 |
| 6  |    34    |    21    | 14.56319  | 0.87265 |
| 7  |    34    |    46    | 14.56319  | 0.46478 |
| 8  |    34    |    46    | 14.56319  | 0.13665 |
| 9  |    46    |    21    | 7.99581   | 0.04189 |
| 10 |    46    |    21    | 7.99581   | 0.91754 |
| 11 |    46    |    34    | 7.99581   | 0.73688 |
| 12 |    46    |    34    | 7.99581   | 0.24299 |'''

def make_table(filename):
    # make sqlite table
    with sqlite3.connect(filename) as con:
        df = pd.read_table(io.BytesIO(text), sep=r'\s*[|]\s*').iloc[:, 1:-1]
        df.to_sql('dataset', con=con, if_exists='replace')

filename = '/tmp/data.sqlite'
make_table(filename)

with sqlite3.connect(filename) as con:
    sql = '''
        SELECT SourceID, TargetID, min(`Values`) as min_value
          FROM dataset
          GROUP BY SourceID, TargetID
    '''
    df = pd.read_sql(sql, con)
    table = df.pivot(index='SourceID', columns='TargetID', values='min_value')

    sql = 'SELECT DISTINCT SourceID FROM dataset ORDER BY Parameter ASC'
    order = pd.read_sql(sql, con)['SourceID']
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

import plotly.io as pio
png_renderer = pio.renderers["png"]
png_renderer.width = 500
png_renderer.height = 500

