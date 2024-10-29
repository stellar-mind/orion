import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Definir o escopo
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Credenciais de serviço
creds = ServiceAccountCredentials.from_json_keyfile_name('./env/compact-pier-440100-u3-731d3c0a0427.json', scope)

# Autenticar e abrir a planilha
client = gspread.authorize(creds)
sheet = client.open("Orion-Origem").sheet1

# Ler dados da planilha
data = sheet.get_all_records()
print(data)