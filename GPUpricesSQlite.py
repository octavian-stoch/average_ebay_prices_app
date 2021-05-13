# ebay gpu prices visualizer
# TODO:// check whether or not the listing is sold: 'sellingState': 'Active'
from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
from pprint import pprint
import matplotlib
import time
from decouple import config
import sqlite3
import re

# SQlite config and code
conn    = sqlite3.connect('database.db')
cursor  = conn.cursor()

# TODO:// create_table_search title based on ebay api keyword search
def universal_create_table(table_name):
    # drop table to start fresh is good practice
    cursor.execute('DROP TABLE ' + str(table_name))
    # make the table with one column to store data from ebay api
    cursor.execute('CREATE TABLE IF NOT EXISTS '+ table_name + 
    ' (price TEXT, title TEXT)')

def universal_data_entry(table_name, values_price, values_title):
    # insert the values from dictionary as one line per entry atm
    cursor.execute('INSERT INTO ' + table_name + '(price, title) VALUES("'+ 
    str(values_price) +'", "' + str(values_title) + '")')
    conn.commit()

###########################################################################
# GPU FUNCTIONS ONLY #
###########################################################################

def gpu_create_table(table_name):
    # drop table to start fresh is good practice
    cursor.execute('DROP TABLE ' + str(table_name))
    # make the table with one column to store data from ebay api
    cursor.execute('CREATE TABLE IF NOT EXISTS '+ table_name + 
    ' (price TEXT, board_partner TEXT, model_name TEXT, title TEXT)')

def gpu_data_entry(table_name, values_price, values_aib, values_model, 
values_title):
    # insert the values from dictionary as one line per entry atm
    cursor.execute('INSERT INTO ' + table_name + '(price, board_partner, '+
    'model_name, title) VALUES("'+
    str(values_price) +'", "' + str(values_aib) + '", "' + str(values_model) +
    '", "' + str(values_title) +'")')
    conn.commit()

###########################################################################
# GPU FUNCTIONS ONLY #
###########################################################################

def close_connections():
    # close connection and cursor after you are done
    cursor.close()
    conn.close()

# environment variable to NOT expose api key
ID_APP = config('ID_APP')

# Keywords = input('what are you searching for? (ex: white piano)\n')
api = finding(appid=ID_APP, config_file=None)
api_request = { 'keywords': "rtx" }
response = api.execute('findItemsByKeywords', api_request).dict()

'''
pprint (response['searchResult']['item'])
response is in form of dicitonary
dict_keys(['ack', 'version', 'timestamp', 'searchResult', 
'paginationOutput', 'itemSearchURL'])
'''

items = response['searchResult']['item']

'''
 price = response['searchResult']['item'][0]['sellingStatus']['currentPrice']
['value']
post_title = response['searchResult']['item'][0]['title']
'''

items = response['searchResult']['item']

# TODO://   custom table creation with whatever the user types in gui/api 
#           search term
gpu_create_table('ebay_GPU')

for item in items:
    gpu_values = item['sellingStatus']['currentPrice']['value'], item['title']

    # case insensitive finding all lower and uppcase board partner names
    aib_title = re.findall(r"(?i)(evga|asus|galax|gigabyte|msi|palit|zotac" +
    "|EVGA|ASUS|GALAX|GIGABYTE|MSI|PALIT|ZOTAC|FOUNDERS|pny|aorus|rog strix)"
    , str(gpu_values[1]))
    # case insensitive find all model names for each item to be added to db
    model_name = re.findall(r"(?i)(3080|3090|3070|3060|2060|2070|2080)",
     str(gpu_values[1]))
    if (aib_title != []):
        res_aib = ' '
        res2_aib = res_aib.join(aib_title)
        if (res2_aib == 'ROG STRIX'):
            res2_aib = 'ASUS'
        
        #TODO://    remember to make sure to only use one model number!
        #           and make proper formatting
        print (model_name)
        
        res_model = model_name
        gpu_data_entry('ebay_GPU', gpu_values[0], res2_aib.upper(), res_model,
        gpu_values[1])
    else:
        aib_title = 'UNSPECIFIED'
        res_model = model_name[0]
        gpu_data_entry('ebay_GPU', gpu_values[0], aib_title, res_model,
         gpu_values[1])

close_connections()
'''
dict_keys(['itemId', 'title', 'globalId', 'primaryCategory', 
'galleryURL', 'viewItemURL', 'autoPay', 'postalCode', 'location', 
'country', 'shippingInfo', 'sellingStatus', 'listingInfo', 
'returnsAccepted', 'condition', 'isMultiVariationListing', 'topRatedListing'])    
'''