# star wars api and matplot lib graphs

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import matplotlib
import swapi
import urllib.request
import json

scope =["https://spreadsheets.google.com/feeds",
'https://www.googleapis.com/auth/spreadsheets',
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope)

client = gspread.authorize(creds)

sheet = client.open("scaling-web-robot").sheet1

# SWAPI get call base url: https://swapi.dev/api/
# SWAPI get call url for people https://swapi.dev/api/people/

with urllib.request.urlopen("https://swapi.dev/api/people/") as url:
    data = json.loads(url.read().decode())
    #pprint(data)

sw_names        = []
sw_hair_color   = []
pos_data        = 0
for people in data["results"]:
    sw_names.append(data["results"][pos_data]["name"])
    sw_hair_color.append(data["results"][pos_data]["hair_color"])
    pos_data +=1

# zip all relevant data into dictionary (combine multiple lists)
sw_data_dict = dict(zip(sw_names,sw_hair_color))

sheet.insert_row(sw_data_dict, 1)