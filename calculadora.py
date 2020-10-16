
import winsound
frequency = 2000
duration = 100

a = int(input('Introduzca un número > '))
b = int(input('Introduzca otro número > '))

while True:
    print('**********************')
    print('{1} Sumar')
    print('{2} Restar')
    print('{3} Multiplicar')
    print('{4} Dividir')
    print('{0} SALIR ')
    print('*********************')
    x=int(input('Elija una opción ='))
    if x==1:
        print(f'Suma de {a} +{b} es igual a = {a+b} ')
    elif x==2:
        print(f'Resta de {a}-{b} es igual a = {a-b}')
    elif x==3:
        print(f'Producto de {a} * {b} es igual a = {a*b}')
    elif x==4:
        print(f'División de {a} / {b} es igual a = {a/b}')
    elif x==0:
        print('Saliendo....')
        winsound.Beep(frequency, duration)
        break 
    else:
        print('Operación desconocida ..')        