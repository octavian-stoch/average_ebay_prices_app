import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import time
import re
import helper
import GPUpricesSQlite
import sqlite3

def runVisualizer():
    gpu_list = []

    # connect to datase
    conn        = sqlite3.connect('database.db')
    cursor      = conn.cursor()

    # query data to be used in modeling (matplotlib)
    cursor.execute('SELECT price, board_partner, model_name FROM ebay_GPU')
    
    #iterate through db and insert into dictionary
    for row in cursor:
        gpu_list.append([row[0], row[1], row[2]])
    
    # sorted set of "model" for use on x-axis

    #TODO plot using "bar" method (unique)
    plt.style.use("fivethirtyeight")
    
    print(gpu_list)
    # plt.bar(gpu_x_model, gpu_y)

    # close all db connections and cursors
    cursor.close()
    conn.close()

    # show the chart
    plt.show()

runVisualizer()