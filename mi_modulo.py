print("¡Hola desde mi_modulo.py!")

def hacer_algo():
    print(f"¡Soy una función y hago algo! {__name__} ooo {__name__}")

if __name__ == "__main__":
    print('Ejecutando como programa principal')
    hacer_algo()

print("¡Adiós desde mi_módulo.py!")  # Debajo del condicional pero fuera del mismo