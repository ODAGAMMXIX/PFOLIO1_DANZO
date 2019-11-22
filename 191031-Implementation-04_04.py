from selenium import webdriver
import time
import os
import shutil
import sqlite3
import pandas as pd

# OPEN URL / ABRE PÁGINA
print('Hi! I´m DANZO. i need some Computers info to start')
chrome = str(input('chromedrive path: '))
#C:\Windows\chromedriver.exe
local = str(input('downloads path: '))
#C:\Users\wamore\Downloads
print('Now i need some informations about what do you want')

#RouboVeiculo
#FurtoVeiculo
#RouboCelular
#Latrocinio
selectcrime = str(input('select type of crime: '))
if selectcrime == 'RouboVeiculo':
    crime = "RouboVeiculo"
elif selectcrime == 'FurtoVeiculo':
    crime = "FurtoVeiculo"
elif selectcrime == 'RouboCelular':
    crime = "RouboCelular"
elif selectcrime == 'Latrocinio':
    crime = "Latrocinio"

selectmonth = str(input('select month: '))
if selectmonth == 'Janeiro':
   month = "1"
elif selectmonth == 'Fevereiro':
    month = "2"
elif selectmonth == 'Março':
    month = "3"
elif selectmonth == 'Abril':
    month = "4"
elif selectmonth == 'Maio':
    month = "5"
elif selectmonth == 'Junho':
    month = "6"
elif selectmonth == 'Julho':
    month = "7"
elif selectmonth == 'Agosto':
    month = "8"
elif selectmonth == 'Setembro':
    month = "9"
elif selectmonth == 'Outubro':
    month = "10"
elif selectmonth == 'Novembro':
    month = "11"
elif selectmonth == 'Dezembro':
    month = "12"

selectyear = str(input('selecione year: '))
if selectyear == '2015':
    year = "15"
elif selectyear == '2016':
    year = "16"
elif selectyear == '2017':
    year = "17"
elif selectyear == '2018':
    year = "18"
elif selectyear == '2019':
    year = "19"
elif selectyear == '2020':
    year = "20"
print('Now i will open the URL to find the archives')
url = 'http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx'
#driver = webdriver.Chrome(executable_path='https://sites.google.com/a/chromium.org/chromedriver/downloads')
# o local do chromedriver.exe varia de pc para pc, se possivel alocar conforme linha abaixo
driver = webdriver.Chrome(executable_path=chrome)
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(3)

name = "20"+year+"_"+month+""

print('Now, I´m choosing the criteria give 4 u.')
driver.find_element_by_xpath("//*[@id='cphBody_btn"+str(crime)+"']").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_filtroDepartamento']").send_keys("DEINTER 1 - SAO JOSE DOS CAMPOS")
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_filtroSeccional']").send_keys("DEL.SEC.S.JOSÉ DOS CAMPOS")
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_filtroDelegacia']").send_keys("05° D.P. S.JOSE DOS CAMPOS")
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_lkAno"+str(year)+"']").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_lkMes"+str(month)+"']").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_ExportarBOLink']").click()
driver.implicitly_wait(1)
time.sleep(3)

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

if crime == 'RouboVeiculo':
    crime = "ROUBO DE VEÍCULOS"
elif crime == 'FurtoVeiculo':
    crime = "FURTO DE VEÍCULOS"
elif crime == 'RouboCelular':
    crime = "ROUBO DE CELULAR"
elif crime == 'Latrocinio':
    crime = "LATROCÍNIO"

#enviando arquivos para o diretório
download = ''+str(local)+'\DadosBO_'+str(name)+'('+str(crime)+').xls'
diretory = ''+str(repository)+'\DadosBO_'+str(name)+'('+str(crime)+').xlsx'
shutil.move(download,diretory)
time.sleep(3)
print('folder OK!')

#criando o banco de dados e enviando informações da tabela para ele
con = sqlite3.connect(danzo+'\danzodb.db')
wb = pd.read_excel(''+str(repository)+'\DadosBO_'+str(name)+'('+str(crime)+').xlsx', sheet_name = None)

for sheet in wb:
    wb[sheet].to_sql(sheet, con, index=False)
con.commit()