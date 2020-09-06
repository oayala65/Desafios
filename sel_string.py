
#Este programa cuenta las sub cadenas que comienzan con 'A' y terminan con'X'. Se puede mejorar siempre
import borra_pantalla
cadena='ADFXADAX'

def Cuenta_Subcadenas(cadena):
    a = 0
    x = 0
    for i in cadena:
        if i == "A":
            a += 1
            #print(f'A es {a}')
        if i == "X":
            x += a
            #print(f'X es {x}')
    print(f'Total de subcadenas que comienzan con A y terminan en X es = {x}')

Cuenta_Subcadenas(cadena)