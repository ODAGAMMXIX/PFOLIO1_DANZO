from flask import Flask, request, render_template
from flask_googlecharts import GoogleCharts, ColumnChart
from danzo import danzo

# Inicializando a instancia principal do Flask e do FlaskGoogleCharts
# Ref flask: http://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
# Ref flask_googlecharts: https://pythonhosted.org/Flask-GoogleCharts/
app = Flask(__name__)
charts = GoogleCharts()
charts.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
# Anotação que gerencia rotas para o Flask interpretá-las
# No caso estamos declarando a rota principal '/'
# Nela vamos capturar dois tipos de requisições HTTP, GET e POST para renderizar nossos templates
# Ref render_template Flask method: http://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
@app.route('/form', methods=['GET', 'POST'])
def form():
    # Se a requisição for POST, que só acontece quando o usuário dá submit no form pegamos os dados do formulário para criar a query no banco dentro do danzo.py
    if request.method == 'POST':
        crime = request.form.get('crime')
        mesInicial = request.form.get('mesInicial')
        mesFinal = request.form.get('mesFinal')
        ano = request.form.get('ano')
        # Com todos os dados coletados chamamos a função danzo para pegar os dados das tabelas dos gráficos de acordo com os filtros 
        # Ref flask_googlecharts github project: https://github.com/wikkiewikkie/flask-googlecharts
        columnChart = ColumnChart("columnChart", options={"title": "Comparativo de nº de ocorrencias por mês", "width": 1200, "height": 600})
        chartData = danzo(crime, mesInicial, mesFinal, ano)
        columnChart.add_column("string", "month")
        columnChart.add_column("number", "ocorrencias")
        columnChart.add_rows(chartData)
        charts.register(columnChart)
        return render_template('chart.html')
    # Caso o usuário entre na página pelo navegador ou atualize a página, aparece na tela o nosso template do formulário
    elif request.method == 'GET':
        return render_template('form.html')

if __name__ == '__main__':
    app.run()