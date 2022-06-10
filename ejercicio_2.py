import statistics

entrada_datos = 0
item = valor = 0
lista_datos = list()

def media(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    
    return (suma / len(lista))

def mediana(lista):
    datos = sorted(lista)
    indice = len(datos) // 2
 
    if len(lista) % 2 != 0:
        return datos[indice]
    
    return ((datos[indice -1] + datos[indice]) / 2)

def rango(lista):
    retorno = "El Rango de la lista es de " + str(min(lista)) + " hasta " + str(max(lista))

    return (retorno)

def desviacion_estandar(lista):
    return (statistics.pstdev(lista))

while (entrada_datos < 20):
    try:
        valor = input("Ingrese la cantidad de datos a cargar: ")

        if valor.isnumeric():
            entrada_datos = int(valor)

            if (entrada_datos < 20):
                print("La cantidad de datos a ingresar debe ser mayor o igual a 20")
                entrada_datos = 0
        else:
            print("El dato ingresado no es númerico")

    except ValueError:
        print("Ingrese un valor valido")
        pass

print("")
while (item < entrada_datos):
    try:
        valor = input("Ingrese el valor " + str(item + 1) + ": ")

        if valor.isnumeric():
            valor = int(valor)
            lista_datos.append(valor)
            item += 1
        else:
            print("El dato ingresado no es númerico")

    except ValueError:
        print("Ingrese un valor valido")
        pass

print("\n\tLa lista de datos cargados son:")
print("\n\t", lista_datos)
print("\tLa media es: ", media(lista_datos))
print("\tLa mediana es: ", mediana(lista_datos))
print("\t" + rango(lista_datos))
print("\tLa desviacion estandar es: ", desviacion_estandar(lista_datos))