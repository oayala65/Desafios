def muestra_keywords(keywords):
    contador = 0
    for kw in keywords:
        print(kw)
        contador += 1
        if contador == 20:
            contador = 0
            input('Mostrar más...')

muestra_keywords()