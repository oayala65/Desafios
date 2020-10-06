datos_veterinaria=[]
alta_animales=0
fallece_animales=0

n=int(input('Cargar el número de animales = '))
for i in range(n):
    name = int(input('Tipo Animal Perro=1 Gato=2 Conejo=3 Aves=4 Otros=0 ='))
    estado_inicial = int(input('Estado inicial 1=sano 2=enfermo 0=fallecido ='))
    estado_final = int(input('Estado FINAL 1=sano 2=enfermo 0=fallecido ='))
    datos_veterinaria.append([name,estado_inicial,estado_final])

for p in range(n):
    if datos_veterinaria[p][1]==2 and datos_veterinaria[p][2]==1:
        alta_animales=alta_animales+1
    else:
        if datos_veterinaria[p][2]==0:
            fallece_animales=fallece_animales+1

perro=0
gato=0
conejo=0
otro=0
aves=0

for s in datos_veterinaria:
  if s[0]==1:
    perro +=1
    
  elif s[0]==2:
    gato +=1
    
  else:
    if s[0]==3:
      conejo +=1
    
    elif s[0]==4:
      aves +=1
    
    if s[0]==0:
      otro +=1


print(f'Alta de animales {alta_animales}')

print(f'Animales fallecidos {fallece_animales}')

print(f'Cantidad de animales por tipo Perro {perro} Gato {gato} Conejo {conejo} Otro {otro} Aves {aves}')