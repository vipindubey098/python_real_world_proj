# First install python barcode Module
from barcode import EAN13
from barcode.writer import ImageWriter

num_of_barcodes = int(input("How many Barcodes you Need? "))
numbers = range(num_of_barcodes)

for i in numbers:
    id = input(" Give 12-Digit numbers for your barcode id: ")
    my_code = EAN13(id, writer=ImageWriter)
    name = input(" Give the name to save barcodes: ")
    my_code.save(name)




