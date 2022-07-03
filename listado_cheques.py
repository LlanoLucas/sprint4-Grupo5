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
    for i in range(7):
        if dni == list_of_rows[i+1][8]:
            nrochek = list_of_rows[i+1][0]
            cuentaorigen = list_of_rows[i+1][3]
            for j in range(7):
                if list_of_rows[j+1][3] == cuentaorigen and list_of_rows[j+1][0] == nrochek:
                    print("ERROR. No se puede repetir el numero de cheque de una misma cuenta")
            print("Encontre dni")
            if salida == 'PANTALLA':
                print(list_of_rows[i+1])
            elif salida == 'CSV':
                print("importar a un archivo cvs (?)")
            else:
                print("El dato de salida no es valido")
        else:
            print("Numero de DNI no encontrado")

