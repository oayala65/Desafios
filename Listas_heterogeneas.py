#Ordenar una lista con datos eterogeneos.

mi_lista = [1, 40, 1.5, 2, "alma", "zapato", "tasa", 'disco', 2.4, 'dos x tres', 80, 4.9]

n = []
b = []
s = []
for x in mi_lista:
  if type(x) is int:
    n.append(x)
  elif type(x) is float:
    b.append(x)
  elif type(x) is str:
    s.append(x)
n.sort()
b.sort()
s.sort()
final = (n + b + s)
print(final)