
palabra_clave=input('Ingrese la palabra clave = ')

claves=[]
with open('C:\GIT\Desafios\Ej 1\keywords.txt') as f:
    f1=list(f)
    if palabra_clave in f1:
        claves.append(palabra_clave)

print(claves,f1)

