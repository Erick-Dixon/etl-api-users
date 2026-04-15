# ETL Pipeline: API -> Python -> n8n -> Google Sheets

Projeto de Engenharia de Dados focado em automação, transformando dados brutos de uma API em informações estruturadas em uma planilha em nuvem.

## O Fluxo
1. **Extração**: Script Python consome dados da API JSONPlaceholder.
2. **Transformação**: Limpeza e normalização (Filtro de campos e e-mails em lowercase).
3. **Carga (Webhook)**: Envio dos dados tratados para o **n8n**.
4. **Automação**: Workflow no n8n processa a entrada e atualiza uma planilha no **Google Sheets**.

## Visual do Workflow (n8n)
![Fluxo n8n](./caminho-da-sua-imagem.png)

## 🛠️ Tecnologias
- **Python** (Requests, python-dotenv)
- **n8n** (Orquestração Low-code)
- **Google Sheets** (Destino final)

## Como rodar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
