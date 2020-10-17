#Escribe un programa que solicite al usuario 5 
# números y, tras ello, muestre cuál es el mayor y cuál es el menor.

a=20
b=8

ma=0
me=0

if a>b:
    ma=a
    me=b
else:
    ma=b
    me=a

c=50

if c>ma:
    ma=c
elif c<me:
    me=c    

k=-1

if k>ma:
    ma=k
elif k<me:
    me=k

d=1

if d>ma:
    ma=d
elif d<me:
    me=d
    
print(f'El numero mayor es {ma} y el menor es {me}')
