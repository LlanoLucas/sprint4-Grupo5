from csv import reader


dni = input("Ingrese un DNI: \n")
salida = input("Ingrese el tipo de salida (PANTALLA o CSV): \n")
tipo = input("Ingrese tipo de cheque (EMITIDO o DEPOSITADO): \n")
#estado = input("Ingrese el estado del cheque (PENDIENTE, APROBADO o RECHAZADO): \n")

with open('test.csv', 'r') as csv_file:
    # Passing the cav_reader object to list() to get a list of lists
    csv_reader = reader(csv_file)
    #convertir el objeto csv.reader en una lista de listas donde cada elemetno de la listasignifica una fila de CSV y cada elemento de la lista representa una celda o columna de una fila
    list_of_rows = list(csv_reader)
    for i in range(8):
        if dni == list_of_rows[i+1][8]:
            print("Encontre dni")
            if salida == 'PANTALLA':
                print(list_of_rows[i+1])
            elif salida == 'CSV':
                #importar a un archivo cvs (?)
            else:
                print("El dato de salida no es valido")
        else:
            print("No encontrado", list_of_rows[i+1][8])

