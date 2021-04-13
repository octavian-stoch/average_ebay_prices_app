import tkinter as tk
import easygui
import visualizer
'''
helper functions
parsing and such, etc...

asus
evga
galax
gigabyte
inno3d
msi
palit
zotac
'''

# convert two lists into dictionary (Key : Value)
# only use this function if not using multiple of the same key
def convertDict(listK, listV, res):
    for key in listK:
        for value in listV:
            res[key] = value
            listV.remove(value)
            break

# https://stackoverflow.com/questions/53782591/how-to-display-actual-
# values-instead-of-percentages-on-my-pie-chart-using-matplo
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format

# https://www.linkedin.com/pulse/creating-app-your-python-
# scripts-tkinter-f%C3%A1bio-neves/