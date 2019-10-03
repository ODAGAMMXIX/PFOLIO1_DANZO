from selenium import webdriver #launch url
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select #dropdown lists
url = 'http://www.ssp.sp.gov.br/estatistica/pesquisa.aspx/'
#driver = webdriver.Chrome(executable_path='https://sites.google.com/a/chromium.org/chromedriver/downloads')
driver = webdriver.Chrome(executable_path='C:\\Users\\Usuario\\OneDrive - Fatec Centro Paula Souza\\19 - FATEC - SJC\\190824 - Projeto Integrador\\chromedriver_win32\\chromedriver.exe')
driver.get(url)
driver.maximize_window()
#driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@id='conteudo_ddlAnos']").send_keys("Todos")
#driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='conteudo_ddlRegioes']").send_keys("São José dos Campos")
#driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='conteudo_ddlMunicipios']").send_keys("São José dos Campos")
#driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='conteudo_ddlDelegacias']").send_keys("05 DP - São Jose dos Campos")
#driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='conteudo_btnExcel']").click()
driver.implicitly_wait(30)