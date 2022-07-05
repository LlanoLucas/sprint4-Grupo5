import csv
import sys

# 1. El script de Python se debe llamar listado_chesques.py
# 2. El orden de los argumentos son los siguientes:
# a. Nombre del archivo csv.
# b. DNI del cliente donde se filtraran.
# c. Salida: PANTALLA o CSV
# d. Tipo de cheque: EMITIDO o DEPOSITADO
# e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)
# f. Rango fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)
# 3. Si para un DNI dado un número de cheque de una misma cuenta se repite se
# debe mostrar el error por pantalla, indicando que ese es el problema.
# 4. Si el parámetro “Salida” es PANTALLA se deberá imprimir por pantalla todos
# los valores que se tienen, y si “Salida” es CSV se deberá exportar a un csv
# con las siguientes condiciones:
# a. El nombre de archivo tiene que tener el formato
# <DNI><TIMESTAMPS ACTUAL>.csv
# b. Se tiene que exportar las dos fechas, el valor del cheque y la cuenta.
# 5. Si el estado del cheque no se pasa, se deberán imprimir los cheques sin
# filtrar por estado 

argumentos = sys.argv[1:]
nombre_archivo = argumentos[0]
dni = argumentos[1]
salida = argumentos[2]
tipo = argumentos[3]

output = []

with open("test.csv", "r") as archivo:
    reader = csv.reader(archivo, delimiter = ",")
    for fila in reader:
        dni_buscado = fila[8]
        tipo_cheque = fila[9]

    if dni_buscado == dni and tipo_cheque == tipo:
        output.append(fila)

if salida == "PANTALLA":
    for fila in output:    
        print(output)
elif salida == "CSV":
    print("falta completar esta parte")
    
        

# linea = archivo.readline()

# buscador = archivo.seek(0)
# print(buscador)