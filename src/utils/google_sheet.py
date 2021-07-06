import os

import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials


load_dotenv(verbose=True)
APIKEY_PATH = os.environ.get("APIKEY_PATH")
SPREADSHEETS_NAME = os.environ.get("SPREADSHEETS_NAME")


def get_sheet(sheet_name):

    scope: list = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(APIKEY_PATH, scope)
    client = gspread.authorize(credentials)
    if credentials.access_token_expired:
        client.login()

    spreadsheets = client.open(SPREADSHEETS_NAME)
    sheet = spreadsheets.worksheet(sheet_name)
    return sheet