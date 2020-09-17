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


for s in range(n):
	if datos_veterinaria[p][0]==1:
 		perro +=1
		return perro
	 else:
 		if datos_veterinaria[p][0]==2:
         	gato +=1
			return gato
     	else:
 			if datos_veterinaria[p][0]==3:
         	conejo +=1
			return conejo

     			else:
 					if datos_veterinaria[p][0]==4:
         				ave +=1
     					return ave
						else:
							if datos_veterinaria[p][0]==0:
         					otro +=1
							return otro 

print(f'Alta de animales {alta_animales}')

print(f'Animales fallecidos {fallece_animales}')

#print(f'Perro {perro} Gato {gato} conejo {conejo} ave {ave} otro{otro}')

print(datos_veterinaria.count(1))
