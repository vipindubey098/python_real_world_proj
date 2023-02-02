import PyPDF2
import csv 
import pandas as pd
import re
from pandas import DataFrame
import SplitRows as SR  # SplitRows.py
import CsvJson as CJ

txt_path = 'new_data.txt'
#add path to csv file 
csv_path = "new_data.csv"     
#add path to json file 
json_path = "new_data.json"


# pdf_file = open("1T00145.pdf", "rb")
pdf_file = open("1T00145A.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# printing number of pages in pdf file
n = int(pdf_reader.numPages)
print("No. of pages: ",n)
# text = pdf_reader.getPage(0).extractText()
#print(text)
file = open('new_data.txt', 'w')
for number in range(n):
    pageObj = pdf_reader.getPage(number)
    data = pageObj.extractText()
    data = re.sub('(\t+|\n+)+', '', data)
    # print(data)
    # data = data.split('----------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------   ') #cbgs to choice mca
    data = data.split('------------------------------------ ----------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------')
    # extracting text from page
    # print(pageObj.extractText())
    # ext.append(len(data))
    print(data[0])
    # found_first_data = data[1]
    # new_data = found_first_data.split('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    # print(new_data[0])
    # print(data[3])
    i = 0
    try:
        # for d in SR.splitEachRow(data[1]):  #cbgs to choicebased
        for d in SR.splitEachRow(data[0]):
            # print(d)
            file.write(d)
            if i % 2 == 0:
                file.write('\t\t|')
            else:
                file.write('\n')
            i += 1
    except:
        print('error')
        continue
file.close()


data=[]
flag=False
with open('new_data.txt','r') as f:
    for line in f:
        if line.startswith('&'):
            flag=True
        if flag:
            data.append(line)
        if line.strip().endswith('!'):
            flag=False

print (''.join(data)) 


# d = CJ.dictList(txt_path)
# # CJ.makeCsv(csv_path, d)
# CJ.makeJson(json_path, d)

# file1=open("1.txt","a")
# file1.writelines(text)