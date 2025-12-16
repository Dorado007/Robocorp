import requests

def run(context):
    url = "https://api.exchangerate.host/latest?base=USD&symbols=COP"
    response = requests.get(url)
    data = response.json()

    rate = data["rates"]["COP"]
    print(f"USD → COP: {rate}")

    context["outputs"]["exchange_rate"] = rate
