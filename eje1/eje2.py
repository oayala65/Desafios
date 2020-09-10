
import requests
from bs4 import BeautifulSoup

# #def aparece_el_dominio(link, dominio):
#     encontrado = False

#     fin = link.find('&')
#     pagina = link[:fin]
#     if dominio in pagina:
#         encontrado = True
#     return encontrado

def comprueba_keywords(kw, dominio):
    continuar = True
    start = 0
    posicion = 1
    encontrado = False
    while continuar and not encontrado:
        parametros = {'q': kw, 'start': start}
        resp = requests.get(f'https://www.google.com/search', params=parametros)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            div_principal = soup.find('div', {'id': 'main'})
            resultados = div_principal.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi')
            for res in resultados:
                if res.div and res.div.a:
                    if aparece_el_dominio(res.div.a['href'], dominio):
                        encontrado = True
                        break
                    else:
                        posicion += 1
            if not encontrado:
                footer = div_principal.find('footer')
                siguiente = footer.find('a', {'aria-label': 'Página siguiente'})
                if siguiente:
                    start += 10
                    if start == 100:
                        continuar = False
                else:
                    continuar = False
        else:
            continuar = False
    if not encontrado:
        posicion = 100
    return posicion

def run():
    keywords = []
    dominio = 'conatel.gov.py'
    
    while True:
        kw = input('Introduzca las palabras clave a comprobar > ')
        posicion = comprueba_keywords(kw, dominio)
        if posicion < 100:
            print(f'Las keywords {kw} se han encontrado en la posición {posicion} para el dominio {dominio}')
        else:
            print(f'De momento, las keywords {kw} no rankean para el dominio {dominio}')

if __name__ == '__main__':
    run()   