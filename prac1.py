s=1

while s<10:
  print(s)
  s +=1
  if s==3:
    print('**************')
  elif s==5:
    print('5*****5')
  elif s==7:
    print('7***********')
  elif s==9:
    print('9********')
print('Terminamos.....')

for item in ['uno','tres','cuatro','1:2:3',(1,2,3)]:
  if item=='tres' or item=='(1,2,3)':
    print(item)