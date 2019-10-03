import requests, bs4
res = requests.get('http://www.ssp.sp.gov.br/Estatistica/Pesquisa.aspx')
print(res.status_code) #status da requisição
file = open("teste.txt", "wb")

for chunk in res.iter_content(100000): #raspagem por blocos
    file.write(chunk) #escrita em blocos no txt
    
try:
    res.raise_for_status() #retorna informações de erro
    objectSoup = bs4.BeautifulSoup(res.text, features = 'lxml') #
    
except Exception as exc: #Exceção do erro
    print(res.text)
    print('Houve um erro: %s' % (exc))



