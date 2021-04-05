# scaling web robot, connecting to google sheets api

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope =["https://spreadsheets.google.com/feeds",
'https://www.googleapis.com/auth/spreadsheets',
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope)

client = gspread.authorize(creds)

sheet = client.open("scaling-web-robot").sheet1

'''
row = sheet.row_values(4)
insertRow = [4, "green"]
sheet.insert_row(insertRow, 4)
'''

data = sheet.get_all_records()
pprint(data)