LIST OF ACADEMIC PROJECTS:

[PROJECT-SEMESTRE-01-2019.2 - *Python Web Scrapper - Public Safety Monitor*](https://github.com/ODAGAMMXIX/PFOLIO1_DANZO) 

[PROJECT-SEMESTRE-02-2020.1 - *Java Stand Alone GANTT Chart tool*](https://github.com/ODAGAMMXIX/PFOLIO2_GANTT)

[PROJECT-SEMESTRE-03-2020.2 - *Java Web App - Benefits According Credit Score*](https://github.com/ODAGAMMXIX/PFOLIO3_VALCODE) 

[PROJECT-SEMESTRE-04-2021.1 - *Oracle HR Solution  for searching candidates via API* ](https://github.com/ODAGAMMXIX/PFOLIO4_JOBNATION) 

[PROJECT-SEMESTRE-05-2021.2 - *Pentaho & Data Warehouse Analytics of Education* ](https://gitlab.com/rafaelEstevam/back-educalytics) 


**FIRST PROJECT, SEMESTRE-01-2019.2 - *Python Web Scrapping - Public Safety Monitor***

![Danzo Logo](https://i.imgur.com/9V0mPnm.png)

**i. ABOUT THIS PROJECT.**

The first project in the first semestre was evolutionary, although hectic.

Without significant contact with the technological resources needed for a working application, there was an imersion in new vocabulary, colleagues and procedures.

Eventually, a web (bot) scrapper was delivered, plotting a heat map of crime in the surrounding of the school, extracting data from the São Paulo State website.

For academic purposes, the description below will be delivered in Portuguese, though I am available to speak about this project in full English should you be interested in hiring me. Here, I acted as P.O. and second S.M. and R&D agent.
 

I - DESCRIÇÃO DO PROJETO.

O primeiro projeto integrador trouxe o tema 'web bot', com liberdade para buscar ferramentas tecnologicas para a efetiva entrega de um Mapeador de Criminalidade ao Redor da FATEC.

Houve dificuldades de natureza humana, estrutural e tecnológica. No primero semestre, encontrando pela primeira vez os colegas e professores, com limitações estruturais e conhecendo novo vocabulário: nomes e neologismos, bem como de gerência de projetos, ambos de TI (metodologia Agile).

Com o suporte de alunos mais experientes do último semestre, os membros da equipe foram revelando suas características e contribuindo livremente com ideias.

Por critério social e utilitarista e no contexto de fatos ocorridos ao redor da FATEC, elegemos um webbot que pudesse mostrar índices de criminalidade nas redonndezas de seu prédio. Ao final, verificamos a possibilidade de comerciaização da solução tanto para o Poder Público como para o mercado imobiliário, securitário, de segurança, transporte e entretenimento em qualquer região do Estado de São Paulo.

Neste semestre, como estréia deste modelo de aprendizado (por projeto), havia ampla liberdade oriunda da amplitude do escopo. Ademais, o processo de criação e aprendizado tem velocidade diferente entre alunos.

Assim, implantamos uma metodologia que denominamos "competing codes". Dois colegas buscavam solução para o mesmo problema, vencendo o código que melhor atendesse as necessidades dos projetos.

Nesse processo, estudamos e aprendemos a respeito de diversas ferramentas e bibliotecas do Python que não foram utilizadas na solução em si (*v.g.* matplotlib).

Ao final, o webbot foi capaz de realizar as seguintes tarefas:

1 - Escolha do usuário na página DANZO;​

2 – Obtenção de dados do sítio Transparência SSP-SP;​

![](imgs/20211026-205948.png)

![](imgs/20211026-210008.png)

![](imgs/20211026-210019.png)

![](imgs/20211026-210044.png)

![](imgs/20211026-210057.png)


3 – Tratamento de arquivo obtido: criação de pasta local, renomeação;​

4 – Tratamento de dados: Leitura do arquivo obtido, coluna por coluna LISTAS), para  inserção em BD;​

![](imgs/20211026-210117.png)

5 – Inserção incremental em BD Sqlite3;​

6 – Leitura do BD Sqlite3;​

7 – Apresentação dos dados: mapa de calor, barras; ​

![](imgs/20211026-210136.png)


**II - TECNOLOGIAS**

Em fase embrionária de aprendizado, a euipe elegeu o Python por ser linguagem de programação de alto nível mais amigável ao programador.

No contexto do Python, contamos com a orientação do Docente e muita pesquisa em fóruns virtuais  especializados para implementar blocos de códigos com propósito específico.

As bibliotecas mais importantes foram:

- selenium: emulação de ações humanas para acessar o sitio da Secretaria de Segurança Pública do Estado de São Paulo, baixando os dados das métricas de crimes em arquivo em formato .CSV, após escolher município, bairro, tipo de crime e período. Escolhemos os crimes contra o patrimônio (furto ou roubo), de aparelhos celulares, automóveis, casas ou estabelecimentos comerciais.

-  pandas: agrupamento de dados por localização, entregando os dados tratados para a apresentação em mapa de calor. Recebemos um curso extracurricular de "Python para Jornalistas", aprendendo as principais funcionalidades para demostrar dados com significância para o usuário final. aqui, nasceu para mim a curiosidade por Ciência de Dados. Com meu conhecimento prévio na área jurídica, tonou-se mais fácil explicar conceitos e etender o que seria mais adequado demonstrar.

-  folium: 
- flask: 
- flask_googlecharts: 

**III - CONTRIBUIÇÕES INDIVIDUAIS.**

A definição do MVP (MINIMUM VIABLE PRODUCT) foi mais simples com minha formação na área jurídica e profissional, tanto no público como no privado.

Nesse passo, a arquitetura ficou assim definnida:
![](imgs/20211026-210335.png)
, 

![](imgs/20211026-202145.png)
Com nosso método de 'competting codes' e com o curso extracurricuar que recebemos na FATEC, consegui chegar ao funcionamento da bibblioteca selenium.

![](imgs/20211026-202416.png)

Então, descobri os drivers que atuam conjuntamente com o *selenium* para emular  ação humana. Elegemos o driver do Googe Chrome, devido à capilaridade:

![](imgs/20211026-204342.png)

Após, descobri que o *sqlite* era o banco de dados mais simples para servir ao nosso *web bot*, na função de mero repositório de dados:
![](imgs/20211026-204544.png)

Conseguir implantar o driver e o selenium para acessar o sítio da SSP-SP:
![](imgs/20211026-204732.png)

Mapeei os campos do sítio da SSP-SP para  que o selenium pudesse atuar  de forma automatizada:
![](imgs/20211026-204907.png)

Enquanto isso, outro colega conseguiu tratar o arquivo para ser inserido no banco de dados:

![](imgs/20211026-205128.png)
(Grande parte desta SPRINT foi utilizada para tentar solucionar esse problema: embora o aqruivo baixado viesse denominado de .CSV, o arquivo possui muitos TABS entre dos dados de forma que, nosso código Python  apresentava erros por buscar uma vírgula como delimitador). 

![](imgs/20211026-205144.png)

Outra colega implantou tratamento de erros e limpeza de arquivos utilizados:
![](imgs/20211026-205241.png)

Tínhamos a expectativa de apenas mostrar gráficos simples e paralelamente, pesquisei a plotagem de mapa de calor. Ao final, os dois 'competing codes' foram implantados:
![](imgs/20211026-205450.png)

![](imgs/20211026-205503.png)


Foi abandonado o *matplotlib* devido à falta de suporte e inadequação dos seus requisitos com o sítio da SSP-SP.

**IV - APRENDIZADOS EFETIVOS.**

Tivemos o primeiro contato com a Metodologia Agil, e com as ferramentas para acompanhamento do projeto: Slack, repositório no Gitlab.

Atuei como segundo Scrum Master, pois o facilitador principal (do último semestre) também possuia carga horária assoberbada; assim, realizávamos nossas *dailys* com a equipe, antes do início das aulas, na biblioteca.

Com isso, comecei a perceber e a desenvolver habilidades de SM e de PO. Também percebi minha capacidade de entender  necessidade do cliente e apresentar o resutado do trabalho da equipe (SM), traduzindo a linguagem técnica em linguagem comercial (venda da solução), destacado pontos fortes que interessam aos clientes e tratando os pontos que podem ser melhorados (PO).

Ao final do projeto, percebemos que a utilização da solução poderia ser aproveitada por muitos recortes sociaisi:

•	Compra/Aluguel de casa;  
•	Abertura de empresas/comércios;  
•	Estudo na região;  
•	Trabalho na região;  
•	Prática esporte na região;  
•	Lazer (evento cultural, maratona geek, ou festa na região);  
•	Morador/Frequentador da região.  

Poteciais clientes pagantes:
-Empresas de segurança: com esses dados poderiam definir uma demanda de vendas/colaboradores por região;  
-Imobiliárias/Construtoras: com esses dados poderiam traçar o perfil de clientes para determinadas regiões;  
-Empreendedores: que teriam acesso a informações sobre o perfil da pessoa que frequenta a região, abrindo um restaurante ou loja que atenda a este público alvo.  

No aspecto técnico, descobri grande habilidade de pesquisa e desenvolvimento (R&D), especialmente na literatura no idioma Inglês, capaz de encontrar rapidamente as ferramentas paa servir à equipe e fomentar a composição de uma solução final.

Com a ajuda de ambientes de colaboração (Google Colab e Jupyter), consegui atingir esta agilidade e os colegas com mais habilidades técnicas de integração nos blocos de códigos contribuiram efetivamente para a inteireza do código fonte final.

Aprendi a utilizar as bibliotecas do Python listadas acima, com razoável velocidade.

Assim, é esperado o aproveitamento desde aprendizado para trabalho comercial técnico em TI, Ciência de Dados para fazer sentido do volume de dados atualmente produzido em todos os setores, bem como na a coordenação de equipes multidisciplianares, em múltiplos idiomas e diversidade cultural.