#Escribe un programa que solicite al usuario que introduzca 10 números y 
# muestre por pantalla cuántos de ellos son pares mayores que 20 y 
# cuántos impares mayores que 50.

i=0
k=j=0
while i<4:
    numero=int(input(f'Introduzca un numero {i} ='))
    if numero % 2==0 and numero>20:
        k +=1
    else:
        if numero % 2!=0 and numero>50:
            j +=1
    i +=1
print(f'Son pares mayor que 20 {k} numeros , y, impares mayores que 50 {j}')
