## PORTFOLIO ACADÊMICO - PROJETOS INTEGRADORES:

## [SEMESTRE-01-2019.2 - *Python-Sqlite3 Web Scrapper - Monitor de Segurança Pública*](https://github.com/ODAGAMMXIX/PFOLIO1_DANZO) 

[SEMESTRE-02-2020.1 - *Java-MySQL Stand Alone App - Gráfico de GANTT para Gestores*](https://github.com/ODAGAMMXIX/PFOLIO2_GANTT)

[SEMESTRE-03-2020.2 - *Java-Oracle - Gamificação, Monetização, Fidelização e Educação Financeira*](https://github.com/ODAGAMMXIX/PFOLIO3_VALCODE)

[SEMESTRE-04-2021.1 - *Java-Oracle API - Recrutamento por Geolocalização et al*](https://github.com/ODAGAMMXIX/PFOLIO4_JOBNATION)

[SEMESTRE-05-2021.2 - *Java-Pentaho-My(SQL)Server-MongoDB-Engajamento Estudantil*](https://github.com/ODAGAMMXIX/PFOLIO5_EDUCALYTICS)

[SEMESTRE-06-2022.1 - *Python-MongoDB-LGPD Opt-in, Opt-out*](https://github.com/ODAGAMMXIX/PFOLIO6_OPTIN_OUT)

***

<h1 align="center">[Python-Sqlite3 Web Scrapper - Monitor de Segurança Pública]</h1>

<p align="center"> 
<img src="https://i.imgur.com/9V0mPnm.png" width="400">
</p>

# **i. ABOUT THIS PORTIFOLIO.**

This portifolio is the result of academic projetcs based on the Learning by Projects method.

For academic purposes, the description below will be delivered in Portuguese, though I am available to speak about this project in full English should you be interested in hiring me. Here, I acted as P.O. and second S.M. and R&D agent.
 

# **I - RESUMO DO PROJETO.**

O primeiro projeto integrador trouxe o tema 'web bot', com liberdade para buscar ferramentas tecnológicas para a efetiva entrega de uma aplicação funcionando. Decidimos por um Mapeador de Criminalidade ao Redor da FATEC.

Houve dificuldades de natureza humana, estrutural e tecnológica. No primeiro semestre, novos colegas e professores, com as limitações de conexão de Internet e de hardware, conhecendo novo vocabulário (neologismos e nomes de artefatos e ferramentas), bem a Metodologia Ágil.

Com o suporte de alunos do último semestre na função de *Scrum Master*, os membros da equipe foram revelando suas características e contribuindo livremente com ideias.

Por critério social e utilitarista e no contexto de fatos ocorridos ao redor da FATEC, elegemos um WebBot.

**Desafio:** Criar um WebBot que mostre índices de criminalidade nas redondezas do *campus*. 

Ao final, **verificamos a possibilidade de comercialização da solução tanto para o Poder Público como para o mercado imobiliário, securitário, de segurança, transporte e entretenimento** em qualquer região do Estado de São Paulo.

Neste semestre, como estréia deste modelo de aprendizado (por projeto), havia ampla liberdade oriunda da amplitude do escopo. Ademais, o processo de criação e aprendizado respeitou a velocidade individual dos alunos.

Assim, implantamos uma metodologia que denominamos ***competing codes***. Dois colegas buscavam solução para o mesmo problema, *vencendo o código que melhor atendesse as necessidades ds projeto*.

Nesse processo, estudamos e aprendemos a respeito de diversas ferramentas e bibliotecas do ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54), que não foram utilizadas na solução em si (*v.g.* Matplotlib).

Ao final, o WebBot foi capaz de realizar as seguintes tarefas:

**1) Opções do usuário na página DANZO (Filtro).** ​

<details><summary>(Clique aqui)</summary>
	<img src="imgs/142784358-5455857c-d84e-48db-bff0-6ef6ff40029a.png" name="1">
</details>

**2) Obtenção de dados do sítio Transparência SSP-SP.** (conforme telas abaixo)

<details><summary>(Clique aqui)</summary>
	<img src="imgs/20211026-205948.png" name="1">
	<img src="imgs/20211026-210008.png" name="2">
	<img src="imgs/20211026-210019.png" name="3">
        <img src="imgs/20211026-210044.png" name="4">
	<img src="imgs/20211026-210057.png" name="5">
</details>


**3) Manuseio do arquivo obtido: criação de pasta local.** (renomeação).​
<details><summary>(Clique aqui)</summary>
Screenshot from 2022-06-18 12-41-19.png
</details>

**4) Tratamento de dados: Leitura do arquivo obtido, coluna por coluna (LISTAS), para  inserção em BD.**

<details><summary>(Clique aqui)​</summary><img src="imgs/20211026-210117.png" name="7"></details>

**5) Inserção incremental em banco de dados** ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white);​

**6) Leitura do BD.** ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white);​

**7) Apresentação dos dados: Filtro escolhido pelo usuário.**

<details><summary> (Clique aqui) ​</summary>
	<img src="imgs/142784358-5455857c-d84e-48db-bff0-6ef6ff40029a.png" name="8">
        <h3 align="center">Fitro para Usuário Escolher</h3></details>
	
**7.1) Apresentação dos dados: Gráfico de barras.**	
<details><summary> (Clique aqui) </summary>
	<img src="imgs/142791377-bc73d39c-81c8-42a1-b372-bcbaaaa0a70b.png" name="9">
	<h3 align="center">Gráfico de Barras 01</h3></details>

**7.2) Apresentação dos dados: Mapa de calor.**
<details><summary> (Clique aqui) </summary>
	<img src="imgs/142784828-959113ea-7464-48f5-bbe3-4c786207929f.png" name="10">
	<h3 align="center">Mapa de Calor</h3></details>




# **II - TECNOLOGIAS**

Em fase embrionária de aprendizado, a equipe elegeu o ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) por ser linguagem de programação de alto nível (mais amigável ao programador).

No contexto do ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54), contamos com a orientação do Docente e muita pesquisa em fóruns virtuais  estrangeiros especializados para implementar blocos de códigos com propósito específico.

As bibliotecas mais importantes do ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) foram:

- ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white): emulação de ações humanas para acessar o sitio da **Secretaria de Segurança Pública do Estado de São Paulo**, baixando os dados das métricas de crimes em arquivo em formato .CSV, após escolher município, bairro, tipo de crime e período. Escolhemos os crimes contra o patrimônio (furto ou roubo), de aparelhos celulares, automóveis, casas ou estabelecimentos comerciais.

- ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white): agrupamento de dados por localização, entregando os dados tratados para a apresentação em mapa de calor. Recebemos um curso extracurricular de "*Python*para Jornalistas", aprendendo as principais funcionalidades para demostrar dados com significância para o usuário final. Aqui, nasceu para mim a curiosidade por Ciência de Dados. **Com meu conhecimento prévio na área jurídica, tonou-se mais fácil explicar conceitos e etender o que seria mais adequado demonstrar**.
	
-  ***Folium***: facilitador de visualização dos dados em um mapa interativo; auxiliou na manipulação dos dados no mapa de calor, com o agrupamento das regiões segundo seus respectivos índices de criminalidade ao redor da Fatec.

- ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white):  Framework para ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) utilizado para desenvolver aplicação web, escolhido pela simplicidade de configuração e rapidez no desenvolvimento, com *curva de aprendizado* mais curta (apresentado pelo *Scrum Master*).

<details><summary>Flask na aplicação</summary><img src="imgs/20211122-201812.png" name="7"></details>
	
- ***flask_googlecharts***: Biblioteca para geração de gráficos (uma das melhores do mercado à época), utilizado no  projeto para gerar aqueles com índice de criminalidade mensal.

- ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white): Pesistência dos dados lidos do arquivo CSV(TAB) oferecido pelo sítio da SSP-SP, pronto para futuras alterações.

# **III - CONTRIBUIÇÕES INDIVIDUAIS.**

Minha formação profissional facilitou a definição do MVP (*Minimum Viable Product*), com a visão de mercado e possibilidade jurídica da ferramenta.

:axe: Como um agente de Pesquisa e Desenvolvimento (*R&D*), realizei a pesquisa em língua estrangeira para desenhar a arquitetura do sistema e fomentar o trabalho dos colegas que, então, implementavam o código. Foi o caso do *Selenium e webdriver, Pandas, SqLite3*.

**Arquitetura**
<details><summary>(Clique aqui)</summary>
	<img src="imgs/20211026-210335.png" name="7">
        <img src="imgs/20211026-202145.png">
</details>

:axe::axe: Com nosso método denominado ***competing codes*** e com o curso extracurricuar sobre ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) que recebemos na FATEC, consegui chegar ao funcionamento da biblioteca ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white).

<details><summary>Selenium.</summary>
<img src="imgs/20211026-202416.png">
</details>

:axe::axe::axe: Então, descobri os *drivers* que atuam conjuntamente com o ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) para emular ação humana. Elegemos o *webdriver* do Googe Chrome, devido à capilaridade.


<details><summary>Webdriver.</summary>
<img src="imgs/20211026-204342.png">
</details>

:axe::axe::axe::axe: Após, descobri que o *SqLite3* era o banco de dados mais simples para servir ao nosso *WebBot*, na função de mero repositório de dados:

<details><summary>SqLite3.</summary>
<img src="imgs/20211026-204544.png">
</details>

	
:axe::axe::axe::axe::axe: Consegui implantar o *webdriver* e o ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) para acessar o sítio da SSP-SP.

<details><summary>Emulação do acesso ao sítio da SSP-SP</summary>
<img src="imgs/20211026-204732.png">
</details>

:axe::axe::axe::axe::axe::axe::axe:Mapeei os campos do sítio da SSP-SP para  que o ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) pudesse atuar  de forma automatizada.

<details><summary>Automação.</summary>
<img src="imgs/20211026-204907.png">
</details>

Enquanto isso, outro colega conseguiu tratar o arquivo para ser inserido no banco de dados:

<details><summary>Inserção BD.</summary>
<img src="imgs/20211026-205128.png">
</details>


(Grande parte desta SPRINT foi utilizada para tentar solucionar esse problema: **embora o arquivo baixado viesse denominado de .CSV, o arquivo possui muitos TABS entre dos dados de forma que, nosso código *Python*  apresentava erros por buscar uma vírgula como delimitador**). 

<details><summary>Delimitador:</summary>
<img src="imgs/20211026-205144.png">
</details>



Outra colega implantou tratamento de erros e limpeza de arquivos utilizados:

<details><summary>Tratamento de erros.</summary>
<img src="imgs/20211026-205241.png">
</details>

Tínhamos a expectativa de apenas mostrar gráficos simples e paralelamente, **pesquisei a plotagem de mapa de calor. Ao final, os dois *competing codes* foram implantados**.

<details><summary>Plotagem.</summary>
<img src="imgs/20211026-205450.png">
<img src="imgs/20211026-205503.png">
</details>

Foi abandonado o *matplotlib* devido à falta de suporte e inadequação dos seus requisitos com o sítio da SSP-SP.

# **IV - APRENDIZADOS EFETIVOS.**

Tivemos o primeiro contato com a *Metodologia Ágil* e com as ferramentas para acompanhamento do projeto: *Slack*, repositório *Git*.

<h3 align="center">SECOND SCRUM MASTER</h3>

Atuei como segundo *Scrum Master* [SM], pois o facilitador principal (do último semestre) também possuia carga horária assoberbada; assim, **realizávamos nossas *dailys* com a equipe, antes do início das aulas, na biblioteca**.Com isso, comecei a perceber e a desenvolver habilidades de SM. 

<h3 align="center">PRODUCT OWNER</h3>
Também percebi minha capacidade de entender  necessidade do cliente como *Product Owner* [PO] e a apresentar o resutado do trabalho da equipe, traduzindo a linguagem técnica em linguagem comercial (venda da solução), destacado pontos fortes que interessam aos clientes e tratando os pontos que podem ser melhorados (PO).

Ao final do projeto, listei a proposta comercial, uma vez verificado que **a solução poderia ser aproveitada para múltiplas finalidades *v.g.*:**
  					
:arrow_right: **Compra/Aluguel de imóveis;**
   
:arrow_right: **Abertura de empresas/comércios;**

:arrow_right: **Geomarketing na região;**

:arrow_right: **Oportunidades de trabalho na região;**

:arrow_right: **Prática esporte na região;**

:arrow_right: **Lazer (evento cultural, maratona *geek*, ou festa na região);** 

:arrow_right: **Morador/Frequentador da região.**

Nessa linha, como **potenciais clientes** pagantes e com nossos dados tratados teríamos:

:heavy_check_mark: **Empresas de segurança:** poderiam definir uma demanda de vendas/colaboradores por região;  

:heavy_check_mark: **Imobiliárias/Construtoras:** poderiam traçar o perfil de clientes para determinadas regiões;  

:heavy_check_mark: **Empreendedores (Geomarketing):** quais negócios abrir na região;

:heavy_check_mark: **Empresas de *Robot Process Automation* [RPA]:** que desejem copiar este modelo de WebBot em qualquer *website* que utilize a mesma arquitetura de *Front End* da SSP-SP (que não disponibilizava *Application programming interface* [API] à época);

<h3 align="center">RESEARCH & DEVELOPMENT</h3>

No aspecto técnico, descobri grande habilidade de pesquisa e desenvolvimento (*R&D*), especialmente no idioma Inglês, capaz de encontrar rapidamente as ferramentas para servir à equipe e fomentar a composição de uma solução final.

Com a ajuda de ambientes de colaboração (*Google Colab e Jupyter*), consegui atingir esta agilidade de respostas, possibilitanddo aos colegas (com mais habilidades técnicas de integração nos blocos de códigos) na escrita e inteireza do código fonte final.

Aprendi a utilizar as bibliotecas do ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) listadas acima, com razoável velocidade.

Assim, é esperado o aproveitamento deste aprendizado para **trabalho comercial técnico em TI, Ciência de Dados para fazer sentido do volume de dados atualmente produzido em todos os setores, bem como na a coordenação de equipes multidisciplianares, em múltiplos idiomas e com diversidade cultural.**

The End.
:arrow_up: 
[`Go Back Up`](#python-sqlite3-web-scrapper---monitor-de-seguran%C3%A7a-p%C3%BAblica).
