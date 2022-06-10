from datetime import datetime

dfecha = datetime.now()
varia_1 = float
varia_2 = float

eventos = {}

def media(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    
    return (round(suma / len(lista), 2))

def total_dias(lista):
    print('\n\tDuraron ' + str(len(lista)) + ' dias en la salida de campo')

def agregar_evento(fecha, num_1, num_2):
    var_min = var_max = 0.0
    if (num_1 < num_2):
        var_min = num_1
        var_max = num_2
    else:
        var_min = num_2
        var_max = num_1
    
    eventos[fecha] = var_min, var_max
    print(eventos)

def eventos_error(lista):
    dias_error = menor_100 = mayor_100 = total_errores = 0
    lista_menor_sin_error = list()
    lista_mayor_sin_error = list()

    for evento in lista.values():
        val_1 = 0
        val_2 = 0
        cont = 0
        for j in evento:
            cont += 1
            if (cont == 1):
                val_1 = j
            else:
                val_2 = j
        
        if (val_1 < 0 or val_2 > 50):
            dias_error += 1
        else:
            lista_menor_sin_error.append(val_1)
            lista_mayor_sin_error.append(val_2)

        if (val_1 < -100):
            menor_100 += 1

        if (val_2 > 100):
            mayor_100 += 1

    total_errores = menor_100 + mayor_100

    lista_menor_sin_error.sort()
    lista_mayor_sin_error.sort()
       
    print("\n\tTotal de dias con errores: ", dias_error)
    print("\tTotal errores menores a -100: ", menor_100)
    print("\tTotal errores mayores a 100: ", mayor_100)
    print("\tTotal errores: ", total_errores)
    print("\n\tMedia minima: ", media(lista_menor_sin_error))
    print("\tMedia maxima: ", media(lista_mayor_sin_error))

while True:
    while True:
        str_fecha = input('\nIngrese fecha de la variacion gravimetricas "dd/mm/aaaa": ')
        
        try:
            dfecha = datetime.strptime(str_fecha, '%d/%m/%Y')
        except ValueError:
            print('\nIngrese una fecha correcta')
        else:
            break

    print('\nPara culminar debe ingresar "0 0" las variaciones gravimetricas para culminar')
    valor = input('Ingrese las variaciones, "separado por un espacio": ')
    try:
        varia_1, varia_2 = (float(item) for item in valor.split())

        if (varia_1 == 0 and varia_2 == 0):
            break

        agregar_evento(dfecha, varia_1, varia_2)

    except ValueError:
        print("Ingresar valores validos")
        pass

total_dias(eventos)
eventos_error(eventos)