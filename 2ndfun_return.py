def suma(num1,num2):
    return num1+num2

def suma1(num1,num2):
    def another_fun(num1,num2):
        return num1+num2
    #return another_fun(num1,num2)

    
total=suma(10,5)
print(suma(10,total))


total1=suma1(10,5)
print(suma1(10,total1))

