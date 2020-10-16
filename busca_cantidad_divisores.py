
lista=[] #La 'lista' es el número que será dividido. k es el divisor.
nlista={} # El diccionario guardará los valores, k=2 para una lista de 1000 numeros es igual a 500

def divisor(k):
    lista.clear()
    n=0
    while n<1000:
        if n % k==0:
            lista.append(n)
        n+=1
    return len(lista)
    
k=1
while k<=20:
    nlista[k]=divisor(k)
    k +=1
    
print(nlista)