from dotenv import load_dotenv

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

def post(dados):
    import requests
    url_webhook = "http://localhost:5678/webhook-test/efb76158-df9c-43a0-ab3f-ffbddc9f3366"
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
