import requests 

AWESOME_URL = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"

def buscar_cotacoes():
    """Busca da cotação atual do dólar e do euro em relação ao real."""
    try:
        response = requests.get(AWESOME_URL, timeout=5) 
        response.raise_for_status()
        data = response.json()
        return {
            "dolar": float(data["USDBRL"]["bid"]),
            "euro": float(data["EURBRL"]["bid"])
        }

    except Exception:
        return None