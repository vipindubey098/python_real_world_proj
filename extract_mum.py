# importing required modules
import PyPDF2  # need to pip install
import re  # need to pip install
import SplitRows as SR  # SplitRows.py
# import CsvJson as CJ

file_path = '1T00145.pdf'
filename = '1T00145.pdf'


def run_main(file_path, filename):
    ext = []
    # creating a pdf file object
    pdf_path = file_path

    pdfFileObj = open(pdf_path, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    n = int(pdfReader.numPages)

    txt_path = "1.txt"  
    
    #add path to csv file 
    csv_path = "1.csv"     
     #add path to json file 
    json_path = "1.json"

    file = open(txt_path, 'w')
    # creating a page object

    for number in range(n):
        pageObj = pdfReader.getPage(number)
        data = pageObj.extractText()
        data = re.sub('(\t+|\n+)+', '', data)
        data = data.split('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        # extracting text from page
        print(pageObj.extractText())
        # ext.append(len(data))
        i = 0
        try:
            for d in SR.splitEachRow(data[3]):
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

    # d = CJ.dictList(txt_path)
    # CJ.makeCsv(csv_path, d)
    # CJ.makeJson(json_path, d)

    # closing the pdf file object
    pdfFileObj.close()