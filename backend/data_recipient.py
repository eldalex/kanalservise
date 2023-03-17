from __future__ import print_function
import os.path
import os
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
import requests
import xml.etree.ElementTree as ET
load_dotenv(override=True)


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# ID Документа подтягивается из env
SAMPLE_SPREADSHEET_ID = os.environ.get('SAMPLESPREADSHEETID')
# Название листа для обработки, подтягивается из env
SAMPLE_RANGE_NAME = os.environ.get('SAMPLERANGENAME')


# Функция получения данных из таблиц google
def get_table():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        if not values:
            print('No data found.')
            return
        else:
            return values
    except HttpError as err:
        print(err)

# Получает курс на текущий день.
def get_course():
    today = datetime.today().strftime('%d/%m/%Y')
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={today}"
    response = requests.get(url)
    # Создаем объект ElementTree из текста ответа
    root = ET.fromstring(response.content)
    # Ищем доллар по ID, и забираем значение.
    dollar = root.find("./Valute[@ID='R01235']")
    if dollar is not None:
        current_course = dollar.find("Value").text
    else:
        dollar = None
    return current_course


# Эту функцию вызывает планировщик, она собирает данные из таблиц, текущий курс, добавляет колонку и отправляет дальше.
def get_new_data():
    current_course = get_course().replace(',', '.')
    table_values = get_table()
    bulk_create_data = []
    for item in table_values[1:]:
        row = {"order_number": int(item[1]),
               "order_cost_in_dollars": int(item[2]),
               "delivery_time": datetime.strptime(item[3], '%d.%m.%Y').date(),
               "order_cost_in_rubles": round(int(item[2]) * float(current_course),2)}
        bulk_create_data.append(row)
    return bulk_create_data
