
student = dict()
n=3
for i in range(n):
  name = input('Nombre =')
  note = float(input('Nota ='))
  student[name] = note

print(student)

reproved=[]
passed=[]

for student,note in student.items():
  if note < 2:
    reproved.append({note,student})
  
  else:
    passed.append({"name": student, "note": note})
  
print(passed)

print(reproved)

