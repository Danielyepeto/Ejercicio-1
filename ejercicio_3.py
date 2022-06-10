# Alumno: Daniel Falcón
#
#
CIEN, CINCUENTA, DIEZ, CINCO = 100, 50, 10, 5
 
cambio = resto = cantidadBilletes = billete = retiro = 0

entrada_dato = True

def es_divisible(numero):
    return (numero % 5 == 0)

while entrada_dato:
    try:
        retiro = input("Ingrese el monto a retirar: ")

        if retiro.isnumeric():
            retiro = int(retiro)
            
            if (not es_divisible(retiro)):
                print("Debe ingresar un monto que sea multiplo de " + str(CINCO))
            else:
                entrada_dato = False
        else:
            print("El dato ingresado no es númerico")

    except ValueError:
        print("Ingrese un valor valido")
        pass

print("\n\tEl monto que ingreso es " + str(retiro) + "$\n")

resto = retiro

while (resto >= 5):
    billete = 0
    if  (resto >= CIEN):
        cantidadBilletes = int(resto / CIEN)
        resto -= (cantidadBilletes * CIEN)
        billete = CIEN
    elif (resto >= CINCUENTA):
        cantidadBilletes = int(resto / CINCUENTA)
        resto -= (cantidadBilletes * CINCUENTA)
        billete = CINCUENTA
    elif (resto >= DIEZ):
        cantidadBilletes = int(resto / DIEZ)
        resto -= (cantidadBilletes * DIEZ)
        billete = DIEZ
    elif (resto >= 5):
        cantidadBilletes = int(resto / CINCO)
        resto -= (cantidadBilletes * CINCO)
        billete = CINCO
    
    print("\t" + str(cantidadBilletes) + " billetes " + str(billete) + "$")