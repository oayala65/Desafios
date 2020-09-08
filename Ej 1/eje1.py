
#palabra_clave=input('Ingrese la palabra clave = ')
def muestra_menu():
    print('')
    print('')
    print('-------- Kwranking --------')
    print('')
    print('[1] – Importar palabras clave')
    print('[2] – Mostrar palabras clave')
    print('[0] – Salir')

def carga_keywords():
    keywords=[]
    with open('C:\GIT\Desafios\Ej 1\keywords.txt') as f:
        f1=list(f)
        for kw in f1:
            kw=kw.replace('\n','')
            keywords.append(kw)
        return keywords
            
def muestra_keywords(keywords):
    contador = 0
    for kw in keywords:
        print(kw)
        contador += 1
        if contador == 20:
            contador = 0
            input('Mostrar más...')

def run():

    keywords = []

    while True:
        muestra_menu()
        opcion = input('Selecciona una opción > ')
        opcion = int(opcion)
        if opcion == 0:
            break
        elif opcion == 1:
            keywords = carga_keywords()
        elif opcion == 2:
            muestra_keywords(keywords)
        else:
            print('Opción no válida')


if __name__ == '__main__':
    run()