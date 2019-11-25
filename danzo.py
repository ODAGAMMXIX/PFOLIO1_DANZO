from selenium import webdriver
import time
import os
import shutil
import sqlite3
import csv
import folium
import pandas as pd
from pathlib import Path
from selenium.webdriver import ChromeOptions, Chrome

month = { 
    "1": "Janeiro", 
    "2": "Fevereiro", 
    "3": "Março", 
    "4": "Abril", 
    "5": "Maio", 
    "6": "Junho", 
    "7": "Julho", 
    "8": "Agosto", 
    "9": "Setembro", 
    "10": "Outubro", 
    "11": "Novembro", 
    "12": "Dezembro"
}

anos = { 
    '2015': '15',
    '2016': '16',
    '2017': '17',
    '2018': '18',
    '2019': '19'
}

crimes = {
    'RouboVeiculo': 'ROUBO DE VEÍCULOS',
    'FurtoVeiculo': 'FURTO DE VEÍCULOS',
    'RouboCelular': 'ROUBO DE CELULAR',
    'Latrocinio': 'LATROCÍNIO'
}

# Definição da função danzo que vai tratar a lógica do web-bot
# Responsável pela utilização do selenium e folium (Heatmap)
# Ref Selenium webdriver: https://selenium.dev/documentation/en/webdriver/
# Ref Folium heatmap: https://python-visualization.github.io/folium/plugins.html
def danzo(crime, mesInicial, mesFinal, ano):
    # Definindo os caminhos dos arquivos usando a lib os
    # Ref Os: https://docs.python.org/3/library/os.html
    danzo = os.getcwd()
    repository = os.getcwd() + '\includes'
    local = str(Path.home()) + '\Downloads'
    chrome = r'C:\Chromedriver\chromedriver.exe'

    table_name = crime
    year = anos[ano]

    conn = sqlite3.connect(danzo + r'\database.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS " + table_name + ";")
    cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (ano_bo,num_bo INTEGER,numero_boletim,bo_iniciado,bo_emitido,dataocorrencia,peridoocorrencia,datacomunicacao,dataelaboracao,bo_autoria,flagrante,numero_boletim_principal,logradouro,numero,bairro,cidade,uf,latitude FLOAT,longitude FLOAT,descricaolocal,exame,solucao,delegacia_nome,delegacia_circunscricao,especie,rubrica,desdobramento,status,nomepessoa,tipopessoa,vitimafatal,rg,rg_uf,naturalidade,nacionalidade,sexo,datanascimento,idade,estadocivil,profissao,grauinstrucao,corcutis,naturezavinculada,tipovinculo,relacionamento,parentesco,placa_veiculo,uf_veiculo,cidade_veiculo,descr_cor_veiculo,descr_marca_veiculo,ano_fabricacao,ano_modelo,descr_tipo_veiculo,quant_celular,marca_celular);")
    listOfMonths = []
    for i in range(int(mesInicial), int(mesFinal) + 1):
        listOfMonths.append(str(i))

    names = []
    for i in range(len(listOfMonths)):
        names.append("20" + year + "_" + listOfMonths[i])

    print('Now i will open the URL to find the archives')
    url = 'http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx'
    # driver = webdriver.Chrome(executable_path='https://sites.google.com/a/chromium.org/chromedriver/downloads')
    # o local do chromedriver.exe varia de pc para pc, se possivel alocar conforme linha abaixo
    driver = webdriver.Chrome(executable_path=chrome)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)

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
    for i in range(len(names)):
        driver.find_element_by_xpath("//*[@id='cphBody_lkMes" + str(listOfMonths[i]) + "']").click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath("//*[@id='cphBody_ExportarBOLink']").click()
        driver.implicitly_wait(1)
        time.sleep(3)

    # fechar a página web
    driver.close()
    
    crime = crimes[crime]

    lista_num_ocorrencias = []
    # enviando arquivos para o diretório
    for i in range(len(names)):
        download = '' + str(local) + '\DadosBO_' + str(names[i]) + '(' + str(crime) + ').xls'
        diretory = '' + str(repository) + '\DadosBO_' + str(names[i]) + '(' + str(crime) + ').xls'
        shutil.move(download, diretory)
        time.sleep(3)

        # criando/conectando o banco de dados
        # tratando o arquivo
        f = open(repository + '\DadosBO_' + str(names[i]) + '(' + str(crime) + ').xls')
        f = f.read()
        f = f.lower().replace('\x00', '').replace(' ', '_').replace('\t', ";").replace(',', '.').replace('latitude','0').replace('longitude', '0').replace('num_bo', '0')
        arquivo = open(repository + '\DadosBO_' + str(names[i]) + '(' + str(crime) + ').csv', 'w')
        arquivo = open(repository + '\DadosBO_' + str(names[i]) + '(' + str(crime) + ').csv', 'w')
        arquivo.write(f)
        arquivo.close()
        len_reader = 0
        
        with open(repository + '\DadosBO_' + str(names[i]) + '(' + str(crime) + ').csv', newline='') as File:
            reader = csv.reader(File, delimiter=';')
            next(reader, None)
            for coluna in reader:
                len_reader += 1 
                lista = []
                for j in range(len(coluna)):
                    lista.append(coluna[j])
                cursor.execute("INSERT INTO " + table_name + " (ano_bo,num_bo,numero_boletim,bo_iniciado,bo_emitido,dataocorrencia,peridoocorrencia,datacomunicacao,dataelaboracao,bo_autoria,flagrante,numero_boletim_principal,logradouro,numero,bairro,cidade,uf,latitude,longitude,descricaolocal,exame,solucao,delegacia_nome,delegacia_circunscricao,especie,rubrica,desdobramento,status,nomepessoa,tipopessoa,vitimafatal,rg,rg_uf,naturalidade,nacionalidade,sexo,datanascimento,idade,estadocivil,profissao,grauinstrucao,corcutis,naturezavinculada,tipovinculo,relacionamento,parentesco,placa_veiculo,uf_veiculo,cidade_veiculo,descr_cor_veiculo,descr_marca_veiculo,ano_fabricacao,ano_modelo,descr_tipo_veiculo,quant_celular,marca_celular) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", lista)
            conn.commit()

        lista_num_ocorrencias.append([month[listOfMonths[i]], len_reader])

        #excluindo .xls e .csv
        myfile = repository + '\DadosBO_' + str(names[i]) + '(' + str(crime) + ').xls'
        ## If file exists, delete it ##
        if os.path.isfile(myfile):
            os.remove(myfile)
        else:  ## Show an error ##
            print("Error: %s file not found" % myfile)
        myfile = repository + '\DadosBO_' + str(names[i]) + '(' + str(crime) + ').csv'
        ## If file exists, delete it ##
        if os.path.isfile(myfile):
            os.remove(myfile)
        else:  ## Show an error ##
            print("Error: %s file not found" % myfile)

    #criando o mapa de calor
    conn = sqlite3.connect(danzo + r'\database.db')
    r = conn.cursor()
    df = pd.read_sql_query("select longitude, latitude from '" + table_name + "' where latitude is not '' and longitude is not '';", conn)
    base_map = folium.Map(location=[-23.208, -45.849], control_scale=True, zoom_start=12)
    from folium.plugins import HeatMap  
    HeatMap(data=df[['latitude', 'longitude']].groupby(['latitude', 'longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(base_map)
    nomes = ''
    for i in range(len(names)):
        nomes += names[i]
    base_map.save(repository + '\DadosBO_' + nomes + '(' + str(crime) + ').html')

    #abrindo o mapa de calor
    url = repository + '\DadosBO_' + nomes + '(' + str(crime) + ').html'
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = Chrome(chrome_options=opts, executable_path=chrome)
    driver.get(url)
    driver.maximize_window()
    return lista_num_ocorrencias