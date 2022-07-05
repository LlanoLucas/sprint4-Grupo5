import csv
import sys

archivo = open("test.csv", "r")
i= 4
for linea in archivo:
    print(i, linea)
    i += 1

# linea = archivo.readline()

# buscador = archivo.seek(0)
# print(buscador)