# Exemplo em Python para autenticar na Google Cloud e consumir a API do Google Sheets por meio de conta de serviço

## Requisitos:
1 - [Python](https://www.python.org/downloads/) 3.10.6 <br>
2 - [gspread](https://docs.gspread.org/en/latest/index.html#gspread) 5.4.0 <br>
3 - __*JSON com as credenciais da conta de serviço salvo na pasta raiz desse repositório com o nome `credentials.json` (A mesma que enviei para o Jhonny e time Americanas)*__

## Start:
— Após clonar esse repositório em seu ambiente de desenvolvimento, use o comando a seguir para instalar os _requirements.txt_ (O gspred já instala por padrão todas as bibliotecas e pacotes do Google necessários): <br>
`pip install -r requirements.txt` <br>
(Por fins de teste, caso não queira usar um arquivo _requirements.txt_ você pode usar diretamente o comando `pip install gspread`).

### Links de referencia:
Visão Geral de Autenticação API Google Cloud <br>
https://cloud.google.com/docs/authentication

Como autenticar como uma conta de serviço <br>
https://cloud.google.com/docs/authentication/production

Referência da API do Google Sheets <br>
https://developers.google.com/sheets/api/reference/rest <br>
https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get <br>

Extras:<br>
https://github.com/googleapis/googleapis.github.io/ <br>
https://googleapis.github.io/google-api-python-client/docs/client-secrets.html
https://developers.google.com/identity/protocols/oauth2/
