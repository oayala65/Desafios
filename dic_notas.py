


reproved=[]
passed=[]
student={}
def muestra_menu():
    print('')
    print('')
    print('-------- Kwranking --------')
    print('')
    print('[1] – Cargar en el diccionario NOMBRE y la NOTA')
    print('[2] – Mostrar los aplazados')
    print('[3] - Mostrar los que aprobaron')
    print('[0] – Salir')

student={}

reproved=[]
passed=[]

def carga_dicc():
  global student
  n=int(input('Cargar el número de estudiantes = '))
  for i in range(n):
    name = input('Nombre =')
    note = int(input('Nota ='))
    student[name] = note

    global reproved
    global passed
       
  for student,note in student.items():
    if note < 2:
      reproved.append({note,student})
  
    else:
      passed.append({"name": student, "note": note})

def muestra_dicc_rep(reproved):
  print(reproved)

def muestra_dicc_apro(pased):
  print(passed)


def principal():
  while True:
    muestra_menu()
    opcion = int(input('Selecciona una opción > '))
    if opcion == 0:
      break
    elif opcion == 1:
      carga_dicc()
    elif opcion == 2:
      muestra_dicc_rep(reproved)
    elif opcion==3:
      muestra_dicc_apro(passed)

    else:
      print('Opción no válida')

if __name__ == '__main__':
  principal()   
