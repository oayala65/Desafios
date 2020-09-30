lista = [['a','b','','','e'],['','3','g'],['']]

new_lista1=[]
item=[]
new_lista=[]
for item in lista:
  for kk in item:
    if kk !='' or kk !=' ':
      new_lista.append(kk)

for cc in new_lista:
  if cc !='':
    new_lista1.append(cc)
print(list(new_lista1))