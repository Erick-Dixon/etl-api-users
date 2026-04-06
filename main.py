def extrair ():
    import requests

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

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
    users_filtrados = []

    for user in users:
        users_filtrados.append({
        "name": user["name"],
        "email": user["email"].lower(),
        "city":user["address"]["city"]
    })
    return users_filtrados

def salvar(dados):
    import json

    with open("output.json","w") as file:
        json.dump(dados, file, indent=2)
def main ():
    dados = extrair()
    dados_tratados = transformar(dados)
    salvar(dados_tratados)

main()
