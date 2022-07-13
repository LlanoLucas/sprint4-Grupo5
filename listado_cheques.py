import csv
import sys
from datetime import datetime


argumentos = sys.argv[1:]
nombre_archivo = argumentos[0]
dni_filtro = argumentos[1]
salida = argumentos[2]
tipo_cheque_filtro = argumentos[3]
estado_filtro = None
rango_fecha = None

if len(argumentos) == 5:
    opcional = argumentos[4]
    tipos_estado = ["PENDIENTE", "APROBADO", "RECHAZADO"]
    if opcional in tipos_estado:
        estado_filtro = opcional
    else:
        rango_fecha = opcional.split(':')
        rango_fecha_ini = datetime.timestamp(datetime.strptime(rango_fecha[0], '%d-%m-%Y'))
        rango_fecha_fin = datetime.timestamp(datetime.strptime(rango_fecha[0], '%d-%m-%Y'))
elif len(argumentos) == 6:
    estado_filtro = argumentos[4]
    rango_fecha = argumentos[5].split(':')
    rango_fecha_ini = datetime.timestamp(datetime.strptime(rango_fecha[0], '%d-%m-%Y'))
    rango_fecha_fin = datetime.timestamp(datetime.strptime(rango_fecha[0], '%d-%m-%Y'))


output = []

with open(nombre_archivo, "r") as archivo:
    reader_csv = csv.reader(archivo, delimiter = ',')
    output.append(next(reader_csv, None))
    for fila in reader_csv:
        fecha = fila[6]
        dni = fila[8]
        tipo_cheque = fila[9]
        estado_cheque = fila[10]
        if dni != dni_filtro or tipo_cheque != tipo_cheque_filtro:
            continue #me salteo la fila y voy a la siguiente
        if estado_filtro is not None and estado_cheque != estado_filtro:
            continue
        if rango_fecha and (fecha < rango_fecha_ini or fecha > rango_fecha_fin):
            continue
        
        output.append(fila)


#no se puede repetir combinacion de mimso DNI NUMERO_CUENTA y NUMERO_CHEQUE
rdos = set()
for nro_fila, fila in enumerate(output):
    nro_cheque = fila[0]
    nro_cuenta = fila[3]
    dni = fila[8]
    if (nro_cheque, nro_cuenta, dni) in rdos:
        output.append(f"Hay inconsistencia en la fila {nro_fila}")
    else:
        rdos.add((nro_cheque, nro_cuenta, dni))



if salida == "PANTALLA":
    for fila in output:    
        print(output)
elif salida == "CSV":
    filtrados = [[fila[3], fila[5], fila[6], fila[7]] for fila in output]
    dt = datetime.now()
    dt = dt.strftime("%d-%m-%Y")
    with open(f'{fila[8]}-{dt}.csv', 'w', newline='') as archivo_salida:
        writer = csv.writer(archivo_salida)
        writer.writerows(filtrados)
