import xlrd
import sqlite3
import pandas as pd

con = sqlite3.connect('C:\\academic-test\\191016-C-danzodb.db')
wb = pd.read_excel('C:\\academic-test\\convertido-append.xlsx',sheet_name = None)

for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False,if_exists='append')
con.commit()
con.close()
