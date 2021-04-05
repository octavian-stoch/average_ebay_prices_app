# ebay gpu prices visualizer

from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import matplotlib
import time
from decouple import config

'''
GOOGLE SHEETS 
OPENING CONNECTIONS FOR READ/WRITE REQUESTS
'''
scope =["https://spreadsheets.google.com/feeds",
'https://www.googleapis.com/auth/spreadsheets',
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope)

client = gspread.authorize(creds)

sheet = client.open("scaling-web-robot")

# select the second worksheet in "scaling-web-robot"
GPUworksheet = sheet.get_worksheet(1)

'''
EBAY API
FINDING GPU PRICES HERE
AND PUT INTO GOOGLE SHEETS USING GSPREAD
'''

ID_APP = config('ID_APP')

# Keywords = input('what are you searching for? (ex: white piano)\n')
api = finding(appid=ID_APP, config_file=None)
api_request = { 'keywords': "rtx" }
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

gpu_dict = {}

for item in items:
    # cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = int(round(float(item.currentprice.string)))
    # url = item.viewitemurl.string.lower()
    gpu_dict.update({title : price})
    GPUworksheet.append_row([title, price])
    time.sleep(3)
    # print('________')
    # print('cat:\n' + cat + '\n')
    # print('title:\n' + title + '\n')
    # print('price:\n' + str(price) + '\n')
    # print('url:\n' + url + '\n')
    # input()


'''
MATPLOT LIB
GRAPHS
'''
