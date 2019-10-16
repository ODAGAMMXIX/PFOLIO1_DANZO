from selenium import webdriver
import time
import os
import shutil


url = 'http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx'
#driver = webdriver.Chrome(executable_path='https://sites.google.com/a/chromium.org/chromedriver/downloads')
# o local do chromedriver.exe varia de pc para pc, se possivel alocar conforme linha abaixo
driver = webdriver.Chrome(executable_path='C:\Windows\chromedriver.exe')
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

#alterar mes e ano
local = r'C:\Users\wamore\Downloads' #local onde o chrome armazena os downloads
month = "8"
year = "19"
name = "20"+year+"_"+month+""

driver.find_element_by_xpath("//*[@id='cphBody_btnRouboVeiculo']").click()
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
time.sleep(10)

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
time.sleep(10)

driver.find_element_by_xpath("//*[@id='cphBody_btnRouboCelular']").click()
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
time.sleep(10)

driver.find_element_by_xpath("//*[@id='cphBody_btnLatrocinio']").click()
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
time.sleep(10)

#fechar a página web
driver.close()

#criando o diretório para armazenar os dados:
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
download = ''+str(local)+'\DadosBO_'+str(name)+'(ROUBO DE VEÍCULOS).xls'
repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(ROUBO DE VEÍCULOS).xls'
shutil.move(download,repository)
time.sleep(3)
download = ''+str(local)+'\DadosBO_'+str(name)+'(FURTO DE VEÍCULOS).xls'
repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(FURTO DE VEÍCULOS).xls'
shutil.move(download,repository)
time.sleep(3)
download = ''+str(local)+'\DadosBO_'+str(name)+'(ROUBO DE CELULAR).xls'
repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(ROUBO DE CELULAR).xls'
shutil.move(download,repository)
time.sleep(3)
download = ''+str(local)+'\DadosBO_'+str(name)+'(LATROCÍNIO).xls'
repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(LATROCÍNIO).xls'
shutil.move(download,repository)
time.sleep(3)



======================

month = 0
while (month < 12):
       print(month)
       month   = month + 1

========================


from selenium import webdriver
import time
import os
import shutil


url = 'http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx'
#driver = webdriver.Chrome(executable_path='https://sites.google.com/a/chromium.org/chromedriver/downloads')
# o local do chromedriver.exe varia de pc para pc, se possivel alocar conforme linha abaixo
driver = webdriver.Chrome(executable_path='C:\Windows\chromedriver.exe')
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

#alterar mes e ano
local = r'C:\Users\wamore\Downloads' #local onde o chrome armazena os downloads
month = 1
month = str(month)
year = "19"
name = "20"+year+"_"+month+""

while (month < 12):

driver.find_element_by_xpath("//*[@id='cphBody_btnRouboVeiculo']").click()
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
time.sleep(10)

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
time.sleep(10)

driver.find_element_by_xpath("//*[@id='cphBody_btnRouboCelular']").click()
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
time.sleep(10)

driver.find_element_by_xpath("//*[@id='cphBody_btnLatrocinio']").click()
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
time.sleep(10)

#criando o diretório para armazenar os dados:
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
download = ''+str(local)+'\DadosBO_'+str(name)+'(ROUBO DE VEÍCULOS).xls'
repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(ROUBO DE VEÍCULOS).xls'
shutil.move(download,repository)
time.sleep(3)
download = ''+str(local)+'\DadosBO_'+str(name)+'(FURTO DE VEÍCULOS).xls'
repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(FURTO DE VEÍCULOS).xls'
shutil.move(download,repository)
time.sleep(3)
download = ''+str(local)+'\DadosBO_'+str(name)+'(ROUBO DE CELULAR).xls'
repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(ROUBO DE CELULAR).xls'
shutil.move(download,repository)
time.sleep(3)
download = ''+str(local)+'\DadosBO_'+str(name)+'(LATROCÍNIO).xls'
repository = r'C:\DANZO\repository\DadosBO_'+str(name)+'(LATROCÍNIO).xls'
shutil.move(download,repository)
time.sleep(3)

month   = month + 1

#fechar a página web
driver.close()











