cadena='ADEXFDSXADXC'
carac='X'


def encuentra(cadena, carac):
  indice = 0
  while indice < len(cadena):
    if cadena[indice] == carac:
      return indice
      indice += 1
  return -1

print(encuentra(cadena,carac))