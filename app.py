from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_exchange_rates():
    url = "https://api.nbp.pl/api/exchangerates/tables/C?format=json"
    response = requests.get(url)
    data = response.json()
    rates = {item['code']: item['ask'] for item in data[0]['rates']} 
    return rates

@app.route('/', methods=['GET', 'POST'])
def index():
    rates = get_exchange_rates()
    cost_in_pln = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        selected_currencies = request.form.getlist('currency')
        total_cost = 0

        for currency in selected_currencies:
            exchange_rate = rates.get(currency)
            if exchange_rate:
                total_cost = round(amount * exchange_rate, 2)

        cost_in_pln = f'{total_cost} zł'

    return render_template('index.html', rates=rates, cost_in_pln=cost_in_pln)

if __name__ == "__main__":
    app.run(debug=True)