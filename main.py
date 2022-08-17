import gspread # gspread https://docs.gspread.org/en/latest/index.html
from google.oauth2 import service_account # Biblioteca que executa a autorização da API OAUTH2 por meio das credenciais de uma Conta de serviço ()

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"] #Escopos https://developers.google.com/identity/protocols/oauth2/scopes?authuser=0#sheets
JSON_FILE = "credentials.json" # Credenciais da Conta de serviço
SPREADSHEET_ID = "1qFjzDvzM8FsQVcwVCCEnGeE-xXy5JiJyaYsGK4mdVUg" # ID da planilha Google Sheets
TAB_NAME = "dados" # Nome da Aba da planilha
DICT = {} # Dicionario Python para manipulação dos valores


#função da biblioteca google.oauth2 que executa a autorização da API OAUTH2 por meio das credenciais da Conta de serviço
def authentication():
    credentials = service_account.Credentials.from_service_account_file(JSON_FILE)
    scoped_credentials = credentials.with_scopes(SCOPES)
    gc = gspread.authorize(scoped_credentials)
    return gc

# Função usando a biblioteca gspread para o método spreadsheets.values.get 
def getspreadsheets():
    gc = authentication()
    planilha = gc.open_by_key(SPREADSHEET_ID)
    tab = planilha.worksheet(TAB_NAME)
    dados = tab.get_all_records()
    # Após termos pego todos os dados da aba escolhida usamos um laço for para armazenar todos os dados em um dicionario para manipulação dos valores
    for dados in planilha:
        DICT[dados.title] = dados.get_all_values()
        print(DICT)

authentication()
getspreadsheets()