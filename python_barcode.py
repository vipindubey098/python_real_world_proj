#first step is to install python barcode module 
from barcode import EAN13 #EAN13 is one of the standard barcode. EAN means European article number
from barcode.writer import ImageWriter # As we know barcode is an image, we need to use this python module to get barcode in image format, so we need to import image writer to convert SVG format to any format of the image.


num_of_barcodes = int(input("How many Barcode you Need?: "))
numbers = range(num_of_barcodes)

# for i in numbers:
#     id = input("Give 12 digit numbers for your barcode id: ")
#     my_code = EAN13(id, writer=ImageWriter())
#     name = input("Give the name to save barcodes: ")
#     my_code.save(name)

for i in numbers:
    id = '98765432125'+str(i)
    #Now, lets create an object of EAN13
    my_code = EAN13(str(id), writer=ImageWriter())
    #print(my_code)
    name = "barcode_"+str(i)
    my_code.save(name)