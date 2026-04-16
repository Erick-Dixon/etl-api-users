from dotenv import load_dotenv
import os

def extrair ():
    import requests
    
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print ("Erro na API")
            return []
        
        return response.json()
    except Exception as e:
        print ("Erro",e)
        return []

def transformar (users):
    return [{
        "name": user["name"],
        "email": user["email"].lower(),
        "city": user["address"]["city"]
    } for user in users]

load_dotenv()

def post(dados):
    import requests
    url_webhook = os.getenv("URL_WEBHOOK")
    try:
        response = requests.post(url_webhook,json=dados)
        print (f"Status: {response.status_code} - Dados enviados!")
    except Exception as e:
        print ("Erro",e)

def main ():
    dados = extrair()
    dados_tratados = transformar(dados)
    post(dados_tratados)

main()
