
import muestra_menu
import muestra_keywords
import carga_keywords

def run():
    keywords = []
    while True:
        muestra_menu
        opcion = input('Selecciona una opción > ')
        opcion = int(opcion)
        if opcion == 0:
            break
        elif opcion == 1:
            keywords = carga_keywords
        elif opcion == 2:
            muestra_keywords()
        else:
            print('Opción no válida')

if __name__ == '__main__':
    run()