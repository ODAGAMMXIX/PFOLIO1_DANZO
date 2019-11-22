from flask import Flask, request, render_template
from flask_googlecharts import GoogleCharts, ColumnChart
from danzo import danzo

charts = GoogleCharts()

app = Flask(__name__)
charts.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        crime = request.form.get('crime')
        mesInicial = request.form.get('mesInicial')
        mesFinal = request.form.get('mesFinal')
        ano = request.form.get('ano')
        columnChart = ColumnChart("columnChart", options={"title": "Comparativo de nº de ocorrencias por mês", "width": 1200, "height": 600})
        chartData = danzo(crime, mesInicial, mesFinal, ano)
        columnChart.add_column("string", "month")
        columnChart.add_column("number", "ocorrencias")
        columnChart.add_rows(chartData)
        charts.register(columnChart)
        return render_template('chart.html')

    return render_template('form.html')

if __name__ == '__main__':
    app.run()