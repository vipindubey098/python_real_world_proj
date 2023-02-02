#import python modules PyPDF2

import PyPDF2
import csv 
import pandas as pd
import SplitRows as SR  # SplitRows.py
from pandas import DataFrame


pdf_file = open("1T00145.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
text = pdf_reader.getPage(0).extractText()
#print(text)
file1=open("1.txt","a")
file1.writelines(text)

# found = False
# with open("1.txt") as openfile:
#      for line in openfile:
#          if not found:
#              counter = 0
#              for part in line.split():
#                   counter = counter + 1
#                   if "====" in part:
#                       print (part)
#                       print (line.split()[counter])
#                       found = True

# mylines = []                             # Declare an empty list named mylines.
# with open ('1.txt', 'rt') as myfile: # Open lorem.txt for reading text data.
#     for myline in myfile:                # For each line, stored as myline,
#         mylines.append(myline)           # add its contents to mylines.
# # print(mylines) 
#     for element in mylines:               # For each element in the list,
#             print(element, end='') 



STARTER = "COURSE I  :"
FILENAME = "1.txt"
TARGET = "--"

with open(FILENAME) as f:
    value = None
    start_seen = False
    for line in f:
        if line.strip() == STARTER:
            start_seen = True
            continue

        if TARGET in line and start_seen:
            _,value = line.split('=')
            break

if value is not None:
    print ("Got value %d" % int(value))
else:
    print ("Nothing found")
