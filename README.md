# PORTFOLIO - LISTA DE PROJETOS ACADÊMICOS:

## [SEMESTRE-01-2019.2 - *Python-Sqlite3 Web Scrapper - Monitor de Segurança Pública*](https://github.com/ODAGAMMXIX/PFOLIO1_DANZO) 

[SEMESTRE-02-2020.1 - *Java-MySQL Stand Alone App - Gráfico de GANTT para Gestores*](https://github.com/ODAGAMMXIX/PFOLIO2_GANTT)

[SEMESTRE-03-2020.2 - *Java-Oracle - Gamificação, Monetização, Fidelização e Educação Financeira*](https://github.com/ODAGAMMXIX/PFOLIO3_VALCODE)

[SEMESTRE-04-2021.1 - *Java-Oracle API - Recrutamento por Geolocalização et al*](https://github.com/ODAGAMMXIX/PFOLIO4_JOBNATION)

[SEMESTRE-05-2021.2 - *Java-Pentaho-My(SQL)Server-MongoDB-Engajamento Estudantil*](https://github.com/ODAGAMMXIX/PFOLIO4_JOBNATION)

[SEMESTRE-06-2022.1 - *Python-MongoDB-LGPD opt-in opt-out ou Análise de Dados Eleitorais *](https://github.com/ODAGAMMXIX/PFOLIO4_JOBNATION)


***

<p align="center">

	## ***[Python-Sqlite3 Web Scrapper - Monitor de Segurança Pública](https://github.com/ODAGAMMXIX/PFOLIO1_DANZO)***
	
</p>
	

![Danzo Logo](https://i.imgur.com/9V0mPnm.png)

# **i. ABOUT THIS PORTIFOLIO.**

This portifolio is the result of academic projetcs based on the Learning by Projects method.

For academic purposes, the description below will be delivered in Portuguese, though I am available to speak about this project in full English should you be interested in hiring me. Here, I acted as P.O. and second S.M. and R&D agent.
 

# **I - RESUMO DO PROJETO.**

O primeiro projeto integrador trouxe o tema 'web bot', com liberdade para buscar ferramentas tecnológicas para a efetiva entrega de uma aplicção funcionando. Decidimos por um Mapeador de Criminalidade ao Redor da FATEC.

Houve dificuldades de natureza humana, estrutural e tecnológica. No primeiro semestre, novos colegas e professores, com as limitações de conexão de Internet e de hardware, conhecendo novo vocabulário (neologismos e nomes de artefatos e ferramentas), bem a Metodologia Ágil.

Com o suporte de alunos do último semestre na função de *Scrum Master*, os membros da equipe foram revelando suas características e contribuindo livremente com ideias.

Por critério social e utilitarista e no contexto de fatos ocorridos ao redor da FATEC, elegemos um WebBot que pudesse mostrar índices de criminalidade nas redondezas do *campus*. Ao final, **verificamos a possibilidade de comercialização da solução tanto para o Poder Público como para o mercado imobiliário, securitário, de segurança, transporte e entretenimento** em qualquer região do Estado de São Paulo.

Neste semestre, como estréia deste modelo de aprendizado (por projeto), havia ampla liberdade oriunda da amplitude do escopo. Ademais, o processo de criação e aprendizado respeitou a velocidade individual dos alunos.

Assim, implantamos uma metodologia que denominamos ***competing codes***. Dois colegas buscavam solução para o mesmo problema, *vencendo o código que melhor atendesse as necessidades ds projeto*.

Nesse processo, estudamos e aprendemos a respeito de diversas ferramentas e bibliotecas do ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54), que não foram utilizadas na solução em si (*v.g.* Matplotlib).

Ao final, o WebBot foi capaz de realizar as seguintes tarefas:

### 1) Escolha do usuário na página DANZO;​
![Entrada](imgs/142784348-aee4f7b9-0949-4a91-a9e6-b8e6ba22415c.png "Entrada")

### 2) Obtenção de dados do sítio Transparência SSP-SP; (conforme telas abaixo);

![](imgs/20211026-205948.png)

![](imgs/20211026-210008.png)

![](imgs/20211026-210019.png)

![](imgs/20211026-210044.png)

![](imgs/20211026-210057.png)

### 3) Manuseio do arquivo obtido: criação de pasta local, renomeação;​

### 4) Tratamento de dados: Leitura do arquivo obtido, coluna por coluna (LISTAS), para  inserção em BD;​

![](imgs/20211026-210117.png)

### 5) Inserção incremental em banco de dados ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white);​

### 6) Leitura do BD ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white);​

### 7) Apresentação dos dados: **mapa de calor e barras, segundo filtro escolhido pelo usuário**; ​

![Fitro para Usuário Escolher](imgs/142784358-5455857c-d84e-48db-bff0-6ef6ff40029a.png  "Fitro para Usuário Escolher")

![Gráfico de Barras 01](imgs/142791377-bc73d39c-81c8-42a1-b372-bcbaaaa0a70b.png  "Gráfico de Barras 01")

![](imgs/20211026-210136.png)

![Mapa de Calor](imgs/142784828-959113ea-7464-48f5-bbe3-4c786207929f.png  "Mapa de Calor")


# **II - TECNOLOGIAS**

Em fase embrionária de aprendizado, a equipe elegeu o ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) por ser linguagem de programação de alto nível (mais amigável ao programador).

No contexto do ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54), contamos com a orientação do Docente e muita pesquisa em fóruns virtuais  estrangeiros especializados para implementar blocos de códigos com propósito específico.

As bibliotecas mais importantes do ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) foram:

- ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white): emulação de ações humanas para acessar o sitio da **Secretaria de Segurança Pública do Estado de São Paulo**, baixando os dados das métricas de crimes em arquivo em formato .CSV, após escolher município, bairro, tipo de crime e período. Escolhemos os crimes contra o patrimônio (furto ou roubo), de aparelhos celulares, automóveis, casas ou estabelecimentos comerciais.

- ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white): agrupamento de dados por localização, entregando os dados tratados para a apresentação em mapa de calor. Recebemos um curso extracurricular de "*Python*para Jornalistas", aprendendo as principais funcionalidades para demostrar dados com significância para o usuário final. Aqui, nasceu para mim a curiosidade por Ciência de Dados. **Com meu conhecimento prévio na área jurídica, tonou-se mais fácil explicar conceitos e etender o que seria mais adequado demonstrar**.
	
-  ***Folium***: facilitador de visualização dos dados em um mapa interativo; auxiliou na manipulação dos dados no mapa de calor, com o agrupamento das regiões segundo seus respectivos índices de criminalidade ao redor da Fatec.

- ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white):  Framework para ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) utilizado para desenvolver aplicação web, escolhido pela simplicidade de configuração e rapidez no desenvolvimento, com *curva de aprendizado* mais curta (apresentado pelo *Scrum Master*).
![](imgs/20211122-201812.png)

- ***flask_googlecharts***: Biblioteca para geração de gráficos (uma das melhores do mercado à época), utilizado no  projeto para gerar aqueles com índice de criminalidade mensal.

- ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white): Pesistência dos dados lidos do arquivo CSV(TAB) oferecido pelo sítio da SSP-SP, pronto para futuras alterações.

# **III - CONTRIBUIÇÕES INDIVIDUAIS.**

Minha formação profissional facilitou a definição do MVP (*Minimum Viable Product*), com a visão de mercado e possibilidade jurídica da ferramenta.

Como um agente de Pesquisa e Desenvolvimento (*R&D*), realizei a pesquisa em língua estrangeira para desenhar a arquitetura do sistema e fomentar o trabalho dos colegas que, então, implementavam o código. Foi o caso do *Selenium e webdriver, Pandas, SqLite3*.

Nesse passo, a arquitetura ficou assim definida:
![](imgs/20211026-210335.png)


![](imgs/20211026-202145.png)

Com nosso método denominado ***competing codes*** e com o curso extracurricuar sobre ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) que recebemos na FATEC, consegui chegar ao funcionamento da biblioteca ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white).

![](imgs/20211026-202416.png)

Então, descobri os *drivers* que atuam conjuntamente com o ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) para emular ação humana. Elegemos o *webdriver* do Googe Chrome, devido à capilaridade:

![](imgs/20211026-204342.png)

Após, descobri que o *SqLite3* era o banco de dados mais simples para servir ao nosso *WebBot*, na função de mero repositório de dados:
![](imgs/20211026-204544.png)

Consegui implantar o *webdriver* e o ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) para acessar o sítio da SSP-SP:
![](imgs/20211026-204732.png)

Mapeei os campos do sítio da SSP-SP para  que o ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) pudesse atuar  de forma automatizada:
![](imgs/20211026-204907.png)

Enquanto isso, outro colega conseguiu tratar o arquivo para ser inserido no banco de dados:

![](imgs/20211026-205128.png)
(Grande parte desta SPRINT foi utilizada para tentar solucionar esse problema: **embora o arquivo baixado viesse denominado de .CSV, o arquivo possui muitos TABS entre dos dados de forma que, nosso código *Python*  apresentava erros por buscar uma vírgula como delimitador**). 

![](imgs/20211026-205144.png)

Outra colega implantou tratamento de erros e limpeza de arquivos utilizados:
![](imgs/20211026-205241.png)

Tínhamos a expectativa de apenas mostrar gráficos simples e paralelamente, **pesquisei a plotagem de mapa de calor. Ao final, os dois *competing codes* foram implantados**:
![](imgs/20211026-205450.png)

![](imgs/20211026-205503.png)


Foi abandonado o *matplotlib* devido à falta de suporte e inadequação dos seus requisitos com o sítio da SSP-SP.

# **IV - APRENDIZADOS EFETIVOS.**

Tivemos o primeiro contato com a *Metodologia Ágil* e com as ferramentas para acompanhamento do projeto: *Slack*, repositório *Git*.

Atuei como segundo *Scrum Master* [SM], pois o facilitador principal (do último semestre) também possuia carga horária assoberbada; assim, **realizávamos nossas *dailys* com a equipe, antes do início das aulas, na biblioteca**.

Com isso, comecei a perceber e a desenvolver habilidades de SM. Também percebi minha capacidade de entender  necessidade do cliente como *Product Owner* [PO] e a apresentar o resutado do trabalho da equipe, traduzindo a linguagem técnica em linguagem comercial (venda da solução), destacado pontos fortes que interessam aos clientes e tratando os pontos que podem ser melhorados (PO).

Ao final do projeto, percebemos que **a solução poderia ser aproveitada para múltiplas finalidades *v.g.*:**

   :arrow_right: **Compra/Aluguel de imóveis; **
   
:arrow_right: **Abertura de empresas/comércios; **

:arrow_right: **Geomarketing na região;  **

:arrow_right: **Oportunidades de trabalho na região;  **

:arrow_right: **Prática esporte na região;  **

:arrow_right: **Lazer (evento cultural, maratona *geek*, ou festa na região); ** 

:arrow_right: **Morador/Frequentador da região. **

Nessa linha, como **potenciais clientes** pagantes e com nossos dados tratados teríamos:

	:heavy_check_mark: **Empresas de segurança:** poderiam definir uma demanda de vendas/colaboradores por região;  

	:heavy_check_mark: **Imobiliárias/Construtoras:** poderiam traçar o perfil de clientes para determinadas regiões;  

:heavy_check_mark: **Empreendedores (Geomarketing):** quais negócios abrir na região;

:heavy_check_mark: **Empresas de *Robot Process Automation* [RPA]:** que desejem copiar este modelo de WebBot em qualquer *website* que utilize a mesma arquitetura de *Front End* da SSP-SP (que não disponibilizava *Application programming interface* [API] à época);

No aspecto técnico, descobri grande habilidade de pesquisa e desenvolvimento (*R&D*), especialmente no idioma Inglês, capaz de encontrar rapidamente as ferramentas para servir à equipe e fomentar a composição de uma solução final.

Com a ajuda de ambientes de colaboração (*Google Colab e Jupyter*), consegui atingir esta agilidade de respostas, possibilitanddo aos colegas (com mais habilidades técnicas de integração nos blocos de códigos) na escrita e inteireza do código fonte final.

Aprendi a utilizar as bibliotecas do ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) listadas acima, com razoável velocidade.

Assim, é esperado o aproveitamento deste aprendizado para **trabalho comercial técnico em TI, Ciência de Dados para fazer sentido do volume de dados atualmente produzido em todos os setores, bem como na a coordenação de equipes multidisciplianares, em múltiplos idiomas e com diversidade cultural.**
