import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import time
import re
import helper

'''
GOOGLE SHEETS 
OPENING CONNECTIONS FOR READ/WRITE REQUESTS
'''
scope =["https://spreadsheets.google.com/feeds",
'https://www.googleapis.com/auth/spreadsheets',
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"]

# create your own secret.json, and paste google sheets creds into it
creds = ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope)

client = gspread.authorize(creds)

sheet = client.open("scaling-web-robot")

# select the second worksheet in "scaling-web-robot"
GPUworksheet = sheet.get_worksheet(1)

'''
MATPLOT LIB 
READ FROM SHEETS AND MAKE GRAPHS
'''

price_data      = GPUworksheet.col_values(2)
ad_titles       = GPUworksheet.col_values(1)

price_data_int  = list(map(int, price_data))
price_data_int.sort()

board_partners  = []

# parsing through all titles
for titles in ad_titles:
    # breaking down each title by aib board partner
    r1 = re.findall(r"(asus|galax|gigabyte|msi|palit|zotac|nvidia)",
    str(titles))
    # if empty, then use a "catch-all"
    if (r1 == []):
        r2 = ['unspecified']
    else:
        r2 = re.findall(r"(asus|galax|gigabyte|msi|palit|zotac|nvidia)",
        str(titles))
    # append only first match, gauranteed to be aib first
    board_partners.append(r2[0])

# TODO//: fix this
# board_partners and price_data_int should be connected via zip
combined_list   = list(zip(board_partners, price_data_int))
sorted_combined = (sorted(combined_list))
# pprint (combined_list)

# pprint (sorted_combined)

averaged_prices = []
filler_value    = 0
count_brands    = 0
first = sorted_combined[0][0] # first brand name in sorted_combined

for values in sorted_combined:
    if first == values[0]:
        filler_value += values[1]
        count_brands += 1
    if first != values[0]:
        averaged_prices.append(first) 
        averaged_prices.append(filler_value // count_brands)
        filler_value = 0
        count_brands = 0
        first = values[0]

updated_brands  = []
updated_average = []
check           = 0

for values in averaged_prices:
    if check == 0:
        updated_brands.append(values)
        check = 1
    else:
        updated_average.append(values)
        check = 0

print (updated_brands, updated_average)


labels          = updated_brands
values          = updated_average
plt.figure(figsize=(5,5))
plt.pie(values, labels = labels, autopct = helper.autopct_format(values))
# plt.pie(values, labels=labels, autopct="%.1f%%")
plt.show()