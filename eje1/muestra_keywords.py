import eje1 as eje 
def muestra_keywords(eje.keywords):
    contador = 0
    for kw in eje.keywords:
        print(kw)
        contador += 1
        if contador == 20:
            contador = 0
            input('Mostrar más...')

muestra_keywords(eje.keywords)