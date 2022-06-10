# Alumno: Daniel Falcón
#
#
ancho_bandera = 0
alto_bandera = 0
entrada_dato = True

def es_par(numero):
    return (numero % 2 == 0)

def imprimir_bandera(ancho, alto):
    linea = ""
    cruz_medio = (ancho / 2) + 0.5
    linea_medio = (alto / 2) + 0.5

    print('\n\tBandera de Inglaterra'.title())
    print("")

    for i in range(alto):
        linea = ""
        for j in range(ancho):
            if (j != (cruz_medio -1) and i != (linea_medio - 1)):
                linea += "O"
            else:
                linea += "+"

        print("\t" + linea)

while entrada_dato:
    try:
        ancho_bandera = input('Ingrese el ancho de la bandera: ')
        alto_bandera = input('Ingrese el alto de la bandera: ')

        if (ancho_bandera.isnumeric() and alto_bandera.isnumeric()):
            ancho_bandera = int(ancho_bandera)
            alto_bandera = int(alto_bandera)
   
            if ((es_par(alto_bandera)) or (es_par(ancho_bandera))):
                print('El largo y el alto de la bandera tiene que ser Numero Impar')
            else:
                entrada_dato = False
                if ((alto_bandera < 2) or (ancho_bandera < 2)):
                    entrada_dato = True
                    print('El largo y el alto de la bandera tiene que ser mayor a 2')
                else:
                    if ((alto_bandera > 20) or (ancho_bandera > 20)):
                        entrada_dato = True
                        print('El largo y el alto de la bandera tiene que ser menor a 20')
        else:
            print("El dato ingresado no es númerico")
        
    except ValueError:
        print("Ingrese un valor valido")
        pass
    
imprimir_bandera(ancho_bandera, alto_bandera)