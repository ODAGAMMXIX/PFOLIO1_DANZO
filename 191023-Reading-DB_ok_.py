import pprint, time, pandas as pd, sqlite3
from sqlite3 import Error
from pandas import DataFrame
conn = None
try:
    conn = sqlite3.connect("C:\\academic-test\\191016-G-danzodb.db")
    print(conn)
except Error as e:
    print(e)
#conn = str()
r = conn.cursor()
#print(r.execute('select * from "DadosBO_2019_8(FURTO DE VEÍCULO"'))
#results = r.fetchall()
#print(r)
df = pd.read_sql_query("select * from 'DadosBO_2019_8(FURTO DE VEÍCULO'", conn)
print(df)
time.sleep(2)
pp = pprint.PrettyPrinter(indent=4, depth=6, width=41, compact=True)
pp.pprint(df)
r.close()
conn.close()
