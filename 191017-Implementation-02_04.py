from selenium import webdriver
import time
import os
import shutil
import xlrd
import sqlite3
import pandas as pd
# OPEN URL / ABRE PÁGINA
print('Hi! I´m DANZO. I´m opening the URL')
url = 'http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx'
#driver = webdriver.Chrome(executable_path='https://sites.google.com/a/chromium.org/chromedriver/downloads')
# o local do chromedriver.exe varia de pc para pc, se possivel alocar conforme linha abaixo
driver = webdriver.Chrome(executable_path='C:\\academic-test\\chromedriver_win32\\chromedriver.exe')
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

#alterar mes e ano
local = r'C:\Users\Usuario\Downloads' #local onde o chrome armazena os downloads
month = "8"
year = "19"
name = "20"+year+"_"+month+""

#driver.find_element_by_xpath("//*[@id='cphBody_btnRouboVeiculo']").click()
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_filtroDepartamento']").send_keys("DEINTER 1 - SAO JOSE DOS CAMPOS")
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_filtroSeccional']").send_keys("DEL.SEC.S.JOSÉ DOS CAMPOS")
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_filtroDelegacia']").send_keys("05° D.P. S.JOSE DOS CAMPOS")
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_lkAno"+str(year)+"']").click()
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_lkMes"+str(month)+"']").click()
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_ExportarBOLink']").click()
#driver.implicitly_wait(30)
#time.sleep(3)

print('Now, I´m choosing the criteria give 4 u.')
driver.find_element_by_xpath("//*[@id='cphBody_btnFurtoVeiculo']").click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='cphBody_filtroDepartamento']").send_keys("DEINTER 1 - SAO JOSE DOS CAMPOS")
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='cphBody_filtroSeccional']").send_keys("DEL.SEC.S.JOSÉ DOS CAMPOS")
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='cphBody_filtroDelegacia']").send_keys("05° D.P. S.JOSE DOS CAMPOS")
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='cphBody_lkAno"+str(year)+"']").click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='cphBody_lkMes"+str(month)+"']").click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='cphBody_ExportarBOLink']").click()
driver.implicitly_wait(30)
time.sleep(3)

#driver.find_element_by_xpath("//*[@id='cphBody_btnRouboCelular']").click()
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_filtroDepartamento']").send_keys("DEINTER 1 - SAO JOSE DOS CAMPOS")
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_filtroSeccional']").send_keys("DEL.SEC.S.JOSÉ DOS CAMPOS")
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_filtroDelegacia']").send_keys("05° D.P. S.JOSE DOS CAMPOS")
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_lkAno"+str(year)+"']").click()
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_lkMes"+str(month)+"']").click()
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_ExportarBOLink']").click()
#driver.implicitly_wait(30)
#time.sleep(3)

#driver.find_element_by_xpath("//*[@id='cphBody_btnLatrocinio']").click()
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_filtroDepartamento']").send_keys("DEINTER 1 - SAO JOSE DOS CAMPOS")
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_filtroSeccional']").send_keys("DEL.SEC.S.JOSÉ DOS CAMPOS")
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_filtroDelegacia']").send_keys("05° D.P. S.JOSE DOS CAMPOS")
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_lkAno"+str(year)+"']").click()
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_lkMes"+str(month)+"']").click()
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='cphBody_ExportarBOLink']").click()
#driver.implicitly_wait(30)
#time.sleep(3)

#fechar a página web
driver.close()

#criando o diretório para armazenar os dados:
print('Creating a folder...')
danzo = r'C:\DANZO'
try:
    os.mkdir(danzo)
except FileExistsError as e:
    print('A pasta DANZO já foi criada!')
repository = r'C:\DANZO\repository'
time.sleep(3)
try:
    os.mkdir(repository)
except FileExistsError as e:
    print('A pasta repository já foi criada!')
time.sleep(3)

#enviando arquivos para o repositório
#download = ''+str(local)+'\DadosBO_'+str(name)+'(ROUBO DE VEÍCULOS).xls'
#repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(ROUBO DE VEÍCULOS).xls'
#shutil.move(download,repository)
#time.sleep(3)
download = ''+str(local)+'\DadosBO_'+str(name)+'(FURTO DE VEÍCULOS).xls'
repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(FURTO DE VEÍCULOS).xls'
shutil.move(download,repository)
time.sleep(3)
#download = ''+str(local)+'\DadosBO_'+str(name)+'(ROUBO DE CELULAR).xls'
#repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(ROUBO DE CELULAR).xls'
#shutil.move(download,repository)
#time.sleep(3)
#download = ''+str(local)+'\DadosBO_'+str(name)+'(LATROCÍNIO).xls'
#repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(LATROCÍNIO).xls'
#shutil.move(download,repository)
#time.sleep(3)

# INSET XLSX INTO DB / INSERE XLSX NO BD
print('Opening the Excel file and inserting it into a Database...')
con = sqlite3.connect('C:\\academic-test\\191016-F-danzodb.db')
wb = pd.read_excel('C:\\DANZO\\repository\\DadosBO_2019_8(FURTO DE VEÍCULOS).xlsx',sheet_name = None)

for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)
con.commit()
con.close()

# SHOW HEADLINE / MOSTRA CABEÇALHO DAS TABELAS
print('Now, I´ll present the data...')
conn = sqlite3.connect(':memory:')

# Import the excel file and call it xls_file
excel_file = pd.ExcelFile(r'C:\DANZO\repository\DadosBO_2019_8(FURTO DE VEÍCULOS).xlsx')

# View the excel_file's sheet names
print(excel_file.sheet_names)

# Load the excel_file's Sheet1 as a dataframe
df = excel_file.parse('DadosBO_2019_8(FURTO DE VEÍCULO')
print(df)


#df = pd.read_excel(r'C:\DANZO\repository\DadosBO_2019_8(FURTO DE VEÍCULOS).xlsx')

#df.rename(columns={'DATAOCORRENCIA': 'DATA_DE_OCORRENCIA','DESCR_MARCA_VEICULO': 'MARCA_DO_VEICULO','PERIDOOCORRENCIA':'PERIODO_DE_OCORRENCIA','DATAELABORACAO': 'DATA_DE_ELABORACAO'}, inplace=True)
df.sample(10)
