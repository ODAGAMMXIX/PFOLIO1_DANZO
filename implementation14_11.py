from selenium import webdriver
import time
import os
import shutil
import sqlite3
import csv
import folium
import pandas as pd

# OPEN URL / ABRE PÁGINA
# criando o diretório para armazenar os dados:
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

print('Hi! I´m DANZO. i need some Computers info to start')
# chrome = str(input('chromedrive path: '))
chrome = r'C:\Windows\chromedriver.exe'
# local = str(input('downloads path: '))
local = r'C:\Users\wamore\Downloads'
print('Now i need some informations about what do you want')

# RouboVeiculo
# FurtoVeiculo
# RouboCelular
# Latrocinio
# selectcrime = str(input('select type of crime: '))
selectcrime = 'RouboVeiculo'
if selectcrime == 'RouboVeiculo':
    crime = "RouboVeiculo"
elif selectcrime == 'FurtoVeiculo':
    crime = "FurtoVeiculo"
elif selectcrime == 'RouboCelular':
    crime = "RouboCelular"
elif selectcrime == 'Latrocinio':
    crime = "Latrocinio"

selectmonth = str(input('select month: '))
#selectmonth = 'Setembro'
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

# selectyear = str(input('selecione year: '))
selectyear = '2019'
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
# driver = webdriver.Chrome(executable_path='https://sites.google.com/a/chromium.org/chromedriver/downloads')
# o local do chromedriver.exe varia de pc para pc, se possivel alocar conforme linha abaixo
driver = webdriver.Chrome(executable_path=chrome)
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(3)

name = "20" + year + "_" + month + ""

print('Now, I´m choosing the criteria give 4 u.')
driver.find_element_by_xpath("//*[@id='cphBody_btn" + str(crime) + "']").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_filtroDepartamento']").send_keys("DEINTER 1 - SAO JOSE DOS CAMPOS")
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_filtroSeccional']").send_keys("DEL.SEC.S.JOSÉ DOS CAMPOS")
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_filtroDelegacia']").send_keys("05° D.P. S.JOSE DOS CAMPOS")
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_lkAno" + str(year) + "']").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_lkMes" + str(month) + "']").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath("//*[@id='cphBody_ExportarBOLink']").click()
driver.implicitly_wait(1)
time.sleep(3)

# fechar a página web
driver.close()

if crime == 'RouboVeiculo':
    crime = "ROUBO DE VEÍCULOS"
elif crime == 'FurtoVeiculo':
    crime = "FURTO DE VEÍCULOS"
elif crime == 'RouboCelular':
    crime = "ROUBO DE CELULAR"
elif crime == 'Latrocinio':
    crime = "LATROCÍNIO"

# enviando arquivos para o diretório
download = '' + str(local) + '\DadosBO_' + str(name) + '(' + str(crime) + ').xls'
diretory = '' + str(repository) + '\DadosBO_' + str(name) + '(' + str(crime) + ').xls'
shutil.move(download, diretory)
time.sleep(3)
print('folder OK!')

# criando/conectando o banco de dados
conn = sqlite3.connect(danzo + r'\database.db')
cursor = conn.cursor()

# criando as tabelas no banco de dados e buscando informações de acordo com o tipo de crime
if crime == "ROUBO DE VEÍCULOS":
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS RouboVeiculo (ano_bo,num_bo INTEGER,numero_boletim,bo_iniciado,bo_emitido,dataocorrencia,peridoocorrencia,datacomunicacao,dataelaboracao,bo_autoria,flagrante,numero_boletim_principal,logradouro,numero,bairro,cidade,uf,latitude FLOAT,longitude FLOAT,descricaolocal,exame,solucao,delegacia_nome,delegacia_circunscricao,especie,rubrica,desdobramento,status,nomepessoa,tipopessoa,vitimafatal,rg,rg_uf,naturalidade,nacionalidade,sexo,datanascimento,idade,estadocivil,profissao,grauinstrucao,corcutis,naturezavinculada,tipovinculo,relacionamento,parentesco,placa_veiculo,uf_veiculo,cidade_veiculo,descr_cor_veiculo,descr_marca_veiculo,ano_fabricacao,ano_modelo,descr_tipo_veiculo,quant_celular,marca_celular);")
    # tratando o arquivo
    f = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').xls')
    f = f.read()
    f = f.lower().replace('\x00', '').replace(' ', '_').replace('\t', ";").replace(',', '.').replace('latitude','0').replace('longitude', '0').replace('num_bo', '0')
    arquivo = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv', 'w')
    arquivo = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv', 'w')
    arquivo.write(f)
    arquivo.close()
    with open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv') as File:
        reader = csv.reader(File, delimiter=';')
        for coluna in reader:
            lista = [(coluna[0]), (coluna[1]), (coluna[2]), (coluna[3]), (coluna[4]), (coluna[5]), (coluna[6]),
                     (coluna[7]), (coluna[8]), (coluna[9]), (coluna[10]), (coluna[11]), (coluna[12]), (coluna[13]),
                     (coluna[14]), (coluna[15]), (coluna[16]), (coluna[17]), (coluna[18]), (coluna[19]), (coluna[20]),
                     (coluna[21]), (coluna[22]), (coluna[23]), (coluna[24]), (coluna[25]), (coluna[26]), (coluna[27]),
                     (coluna[28]), (coluna[29]), (coluna[30]), (coluna[31]), (coluna[32]), (coluna[33]), (coluna[34]),
                     (coluna[35]), (coluna[36]), (coluna[37]), (coluna[38]), (coluna[39]), (coluna[40]), (coluna[41]),
                     (coluna[42]), (coluna[43]), (coluna[44]), (coluna[45]), (coluna[46]), (coluna[47]), (coluna[48]),
                     (coluna[49]), (coluna[50]), (coluna[51]), (coluna[52]), (coluna[53]), (coluna[54]), (coluna[55])]
            cursor.execute("""INSERT INTO RouboVeiculo (ano_bo,num_bo,numero_boletim,bo_iniciado,bo_emitido,dataocorrencia,peridoocorrencia,datacomunicacao,dataelaboracao,bo_autoria,flagrante,numero_boletim_principal,logradouro,numero,bairro,cidade,uf,latitude,longitude,descricaolocal,exame,solucao,delegacia_nome,delegacia_circunscricao,especie,rubrica,desdobramento,status,nomepessoa,tipopessoa,vitimafatal,rg,rg_uf,naturalidade,nacionalidade,sexo,datanascimento,idade,estadocivil,profissao,grauinstrucao,corcutis,naturezavinculada,tipovinculo,relacionamento,parentesco,placa_veiculo,uf_veiculo,cidade_veiculo,descr_cor_veiculo,descr_marca_veiculo,ano_fabricacao,ano_modelo,descr_tipo_veiculo,quant_celular,marca_celular)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""", lista)
        conn.commit()

    #excluindo .xls e .csv
    myfile = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').xls'
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:  ## Show an error ##
        print("Error: %s file not found" % myfile)
    myfile = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv'
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:  ## Show an error ##
        print("Error: %s file not found" % myfile)

    #criando o mapa de calor
    conn = sqlite3.connect(danzo + r'\database.db')
    r = conn.cursor()
    df = pd.read_sql_query("select longitude,latitude,num_bo,bo_emitido from 'RouboVeiculo'", conn)
    from folium.plugins import HeatMap
    def generateBaseMap(default_location=[-23.208, -45.849], default_zoom_start=12):
        base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
        return base_map
    df_copy = df['bo_emitido'].copy()
    df_copy['num_bo'] = 1
    base_map = generateBaseMap()
    HeatMap(data=df[['latitude', 'longitude', 'num_bo']].groupby(
        ['latitude', 'longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(base_map)
    base_map.save(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').html')

    #abrindo o mapa de calor
    url = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').html'
    driver = webdriver.Chrome(executable_path=chrome)
    driver.get(url)
    driver.maximize_window()

elif crime == 'FURTO DE VEÍCULOS':
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS FurtoVeiculo (ano_bo,num_bo INTEGER,numero_boletim,bo_iniciado,bo_emitido,dataocorrencia,peridoocorrencia,datacomunicacao,dataelaboracao,bo_autoria,flagrante,numero_boletim_principal,logradouro,numero,bairro,cidade,uf,latitude FLOAT,longitude FLOAT,descricaolocal,exame,solucao,delegacia_nome,delegacia_circunscricao,especie,rubrica,desdobramento,status,nomepessoa,tipopessoa,vitimafatal,rg,rg_uf,naturalidade,nacionalidade,sexo,datanascimento,idade,estadocivil,profissao,grauinstrucao,corcutis,naturezavinculada,tipovinculo,relacionamento,parentesco,placa_veiculo,uf_veiculo,cidade_veiculo,descr_cor_veiculo,descr_marca_veiculo,ano_fabricacao,ano_modelo,descr_tipo_veiculo,quant_celular,marca_celular);")
    # tratando o arquivo
    f = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').xls')
    f = f.read()
    f = f.lower().replace('\x00', '').replace(' ', '_').replace('\t', ";").replace(',', '.').replace('latitude','0').replace('longitude', '0').replace('num_bo', '0')
    arquivo = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv', 'w')
    arquivo = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv', 'w')
    arquivo.write(f)
    arquivo.close()
    with open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv') as File:
        reader = csv.reader(File, delimiter=';')
        for coluna in reader:
            lista = [(coluna[0]), (coluna[1]), (coluna[2]), (coluna[3]), (coluna[4]), (coluna[5]), (coluna[6]),
                     (coluna[7]), (coluna[8]), (coluna[9]), (coluna[10]), (coluna[11]), (coluna[12]), (coluna[13]),
                     (coluna[14]), (coluna[15]), (coluna[16]), (coluna[17]), (coluna[18]), (coluna[19]), (coluna[20]),
                     (coluna[21]), (coluna[22]), (coluna[23]), (coluna[24]), (coluna[25]), (coluna[26]), (coluna[27]),
                     (coluna[28]), (coluna[29]), (coluna[30]), (coluna[31]), (coluna[32]), (coluna[33]), (coluna[34]),
                     (coluna[35]), (coluna[36]), (coluna[37]), (coluna[38]), (coluna[39]), (coluna[40]), (coluna[41]),
                     (coluna[42]), (coluna[43]), (coluna[44]), (coluna[45]), (coluna[46]), (coluna[47]), (coluna[48]),
                     (coluna[49]), (coluna[50]), (coluna[51]), (coluna[52]), (coluna[53]), (coluna[54]), (coluna[55])]
            cursor.execute("""INSERT INTO FurtoVeiculo (ano_bo,num_bo,numero_boletim,bo_iniciado,bo_emitido,dataocorrencia,peridoocorrencia,datacomunicacao,dataelaboracao,bo_autoria,flagrante,numero_boletim_principal,logradouro,numero,bairro,cidade,uf,latitude,longitude,descricaolocal,exame,solucao,delegacia_nome,delegacia_circunscricao,especie,rubrica,desdobramento,status,nomepessoa,tipopessoa,vitimafatal,rg,rg_uf,naturalidade,nacionalidade,sexo,datanascimento,idade,estadocivil,profissao,grauinstrucao,corcutis,naturezavinculada,tipovinculo,relacionamento,parentesco,placa_veiculo,uf_veiculo,cidade_veiculo,descr_cor_veiculo,descr_marca_veiculo,ano_fabricacao,ano_modelo,descr_tipo_veiculo,quant_celular,marca_celular)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",lista)
        conn.commit()

    # excluindo .xls e .csv
    myfile = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').xls'
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:  ## Show an error ##
        print("Error: %s file not found" % myfile)
    myfile = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv'
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:  ## Show an error ##
        print("Error: %s file not found" % myfile)

    # criando o mapa de calor
    conn = sqlite3.connect(danzo + r'\database.db')
    r = conn.cursor()
    df = pd.read_sql_query("select longitude,latitude,num_bo,bo_emitido from 'FurtoVeiculo'", conn)
    from folium.plugins import HeatMap
    def generateBaseMap(default_location=[-23.208, -45.849], default_zoom_start=12):
        base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
        return base_map
    df_copy = df['bo_emitido'].copy()
    df_copy['num_bo'] = 1
    base_map = generateBaseMap()
    HeatMap(data=df[['latitude', 'longitude', 'num_bo']].groupby(
        ['latitude', 'longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(base_map)
    base_map.save(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').html')

    # abrindo o mapa de calor
    url = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').html'
    driver = webdriver.Chrome(executable_path=chrome)
    driver.get(url)
    driver.maximize_window()

elif crime == 'ROUBO DE CELULAR':
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS RouboCelular (ano_bo,num_bo INTEGER,numero_boletim,bo_iniciado,bo_emitido,dataocorrencia,peridoocorrencia,datacomunicacao,dataelaboracao,bo_autoria,flagrante,numero_boletim_principal,logradouro,numero,bairro,cidade,uf,latitude FLOAT,longitude FLOAT,descricaolocal,exame,solucao,delegacia_nome,delegacia_circunscricao,especie,rubrica,desdobramento,status,nomepessoa,tipopessoa,vitimafatal,rg,rg_uf,naturalidade,nacionalidade,sexo,datanascimento,idade,estadocivil,profissao,grauinstrucao,corcutis,naturezavinculada,tipovinculo,relacionamento,parentesco,placa_veiculo,uf_veiculo,cidade_veiculo,descr_cor_veiculo,descr_marca_veiculo,ano_fabricacao,ano_modelo,descr_tipo_veiculo,quant_celular,marca_celular);")
    # tratando o arquivo
    f = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').xls')
    f = f.read()
    f = f.lower().replace('\x00', '').replace(' ', '_').replace('\t', ";").replace(',', '.').replace('latitude','0').replace('longitude', '0').replace('num_bo', '0')
    arquivo = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv', 'w')
    arquivo = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv', 'w')
    arquivo.write(f)
    arquivo.close()
    with open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv') as File:
        reader = csv.reader(File, delimiter=';')
        for coluna in reader:
            lista = [(coluna[0]), (coluna[1]), (coluna[2]), (coluna[3]), (coluna[4]), (coluna[5]), (coluna[6]),
                     (coluna[7]), (coluna[8]), (coluna[9]), (coluna[10]), (coluna[11]), (coluna[12]), (coluna[13]),
                     (coluna[14]), (coluna[15]), (coluna[16]), (coluna[17]), (coluna[18]), (coluna[19]), (coluna[20]),
                     (coluna[21]), (coluna[22]), (coluna[23]), (coluna[24]), (coluna[25]), (coluna[26]), (coluna[27]),
                     (coluna[28]), (coluna[29]), (coluna[30]), (coluna[31]), (coluna[32]), (coluna[33]), (coluna[34]),
                     (coluna[35]), (coluna[36]), (coluna[37]), (coluna[38]), (coluna[39]), (coluna[40]), (coluna[41]),
                     (coluna[42]), (coluna[43]), (coluna[44]), (coluna[45]), (coluna[46]), (coluna[47]), (coluna[48]),
                     (coluna[49]), (coluna[50]), (coluna[51]), (coluna[52]), (coluna[53]), (coluna[54]), (coluna[55])]
            cursor.execute("""INSERT INTO RouboCelular (ano_bo,num_bo,numero_boletim,bo_iniciado,bo_emitido,dataocorrencia,peridoocorrencia,datacomunicacao,dataelaboracao,bo_autoria,flagrante,numero_boletim_principal,logradouro,numero,bairro,cidade,uf,latitude,longitude,descricaolocal,exame,solucao,delegacia_nome,delegacia_circunscricao,especie,rubrica,desdobramento,status,nomepessoa,tipopessoa,vitimafatal,rg,rg_uf,naturalidade,nacionalidade,sexo,datanascimento,idade,estadocivil,profissao,grauinstrucao,corcutis,naturezavinculada,tipovinculo,relacionamento,parentesco,placa_veiculo,uf_veiculo,cidade_veiculo,descr_cor_veiculo,descr_marca_veiculo,ano_fabricacao,ano_modelo,descr_tipo_veiculo,quant_celular,marca_celular)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",lista)
        conn.commit()

    # excluindo .xls e .csv
    myfile = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').xls'
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:  ## Show an error ##
        print("Error: %s file not found" % myfile)
    myfile = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv'
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:  ## Show an error ##
        print("Error: %s file not found" % myfile)

    # criando o mapa de calor
    conn = sqlite3.connect(danzo + r'\database.db')
    r = conn.cursor()
    df = pd.read_sql_query("select longitude,latitude,num_bo,bo_emitido from 'RouboCelular'", conn)
    from folium.plugins import HeatMap
    def generateBaseMap(default_location=[-23.208, -45.849], default_zoom_start=12):
        base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
        return base_map
    df_copy = df['bo_emitido'].copy()
    df_copy['num_bo'] = 1
    base_map = generateBaseMap()
    HeatMap(data=df[['latitude', 'longitude', 'num_bo']].groupby(
        ['latitude', 'longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(base_map)
    base_map.save(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').html')

    # abrindo o mapa de calor
    url = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').html'
    driver = webdriver.Chrome(executable_path=chrome)
    driver.get(url)
    driver.maximize_window()


elif crime == 'LATROCÍNIO':
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Latrocinio (ano_bo,num_bo INTEGER,numero_boletim,bo_iniciado,bo_emitido,dataocorrencia,peridoocorrencia,datacomunicacao,dataelaboracao,bo_autoria,flagrante,numero_boletim_principal,logradouro,numero,bairro,cidade,uf,latitude FLOAT,longitude FLOAT,descricaolocal,exame,solucao,delegacia_nome,delegacia_circunscricao,especie,rubrica,desdobramento,status,nomepessoa,tipopessoa,vitimafatal,rg,rg_uf,naturalidade,nacionalidade,sexo,datanascimento,idade,estadocivil,profissao,grauinstrucao,corcutis,naturezavinculada,tipovinculo,relacionamento,parentesco,placa_veiculo,uf_veiculo,cidade_veiculo,descr_cor_veiculo,descr_marca_veiculo,ano_fabricacao,ano_modelo,descr_tipo_veiculo,quant_celular,marca_celular);")
    # tratando o arquivo
    f = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').xls')
    f = f.read()
    f = f.lower().replace('\x00', '').replace(' ', '_').replace('\t', ";").replace(',', '.').replace('latitude','0').replace('longitude', '0').replace('num_bo', '0')
    arquivo = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv', 'w')
    arquivo = open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv', 'w')
    arquivo.write(f)
    arquivo.close()
    with open(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv') as File:
        reader = csv.reader(File, delimiter=';')
        for coluna in reader:
            lista = [(coluna[0]), (coluna[1]), (coluna[2]), (coluna[3]), (coluna[4]), (coluna[5]), (coluna[6]),
                     (coluna[7]), (coluna[8]), (coluna[9]), (coluna[10]), (coluna[11]), (coluna[12]), (coluna[13]),
                     (coluna[14]), (coluna[15]), (coluna[16]), (coluna[17]), (coluna[18]), (coluna[19]), (coluna[20]),
                     (coluna[21]), (coluna[22]), (coluna[23]), (coluna[24]), (coluna[25]), (coluna[26]), (coluna[27]),
                     (coluna[28]), (coluna[29]), (coluna[30]), (coluna[31]), (coluna[32]), (coluna[33]), (coluna[34]),
                     (coluna[35]), (coluna[36]), (coluna[37]), (coluna[38]), (coluna[39]), (coluna[40]), (coluna[41]),
                     (coluna[42]), (coluna[43]), (coluna[44]), (coluna[45]), (coluna[46]), (coluna[47]), (coluna[48]),
                     (coluna[49]), (coluna[50]), (coluna[51]), (coluna[52]), (coluna[53]), (coluna[54]), (coluna[55])]
            cursor.execute("""INSERT INTO Latrocinio (ano_bo,num_bo,numero_boletim,bo_iniciado,bo_emitido,dataocorrencia,peridoocorrencia,datacomunicacao,dataelaboracao,bo_autoria,flagrante,numero_boletim_principal,logradouro,numero,bairro,cidade,uf,latitude,longitude,descricaolocal,exame,solucao,delegacia_nome,delegacia_circunscricao,especie,rubrica,desdobramento,status,nomepessoa,tipopessoa,vitimafatal,rg,rg_uf,naturalidade,nacionalidade,sexo,datanascimento,idade,estadocivil,profissao,grauinstrucao,corcutis,naturezavinculada,tipovinculo,relacionamento,parentesco,placa_veiculo,uf_veiculo,cidade_veiculo,descr_cor_veiculo,descr_marca_veiculo,ano_fabricacao,ano_modelo,descr_tipo_veiculo,quant_celular,marca_celular)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""", lista)
        conn.commit()

    # excluindo .xls e .csv
    myfile = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').xls'
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:  ## Show an error ##
        print("Error: %s file not found" % myfile)
    myfile = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').csv'
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:  ## Show an error ##
        print("Error: %s file not found" % myfile)

    # criando o mapa de calor
    conn = sqlite3.connect(danzo + r'\database.db')
    r = conn.cursor()
    df = pd.read_sql_query("select longitude,latitude,num_bo,bo_emitido from 'Latrocinio'", conn)
    from folium.plugins import HeatMap
    def generateBaseMap(default_location=[-23.208, -45.849], default_zoom_start=12):
        base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
        return base_map
    df_copy = df['bo_emitido'].copy()
    df_copy['num_bo'] = 1
    base_map = generateBaseMap()
    HeatMap(data=df[['latitude', 'longitude', 'num_bo']].groupby(
        ['latitude', 'longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(base_map)
    base_map.save(repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').html')

    # abrindo o mapa de calor
    url = repository + '\DadosBO_' + str(name) + '(' + str(crime) + ').html'
    driver = webdriver.Chrome(executable_path=chrome)
    driver.get(url)
    driver.maximize_window()


