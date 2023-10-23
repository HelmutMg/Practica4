import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Verificar si hubo errores en la solicitud
        bitcoin_data = response.json()
        return bitcoin_data['bpi']['USD']['rate_float']
    except requests.RequestException as e:
        print(f"Error al consultar la API de CoinDesk: {e}")
        return None

def main():
    n = input("Ingrese la cantidad de bitcoins que posee: ")
    
    try:
        n_bitcoins = float(n)
    except ValueError:
        print("Por favor, ingrese un valor válido para la cantidad de bitcoins.")
        return
    
    bitcoin_price = get_bitcoin_price()
    if bitcoin_price is not None:
        cost_in_usd = n_bitcoins * bitcoin_price
        formatted_cost = f"${cost_in_usd:,.4f}"
        print(f"El costo actual de {n_bitcoins:.4f} Bitcoins es {formatted_cost} USD.")

if __name__ == "__main__":
    main()
