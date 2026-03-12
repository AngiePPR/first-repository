# hello.py
# Programa simple para probar un repositorio en GitHub

def saludar(nombre):
    print(f"Hola, {nombre}! Bienvenida a tu primer repositorio en GitHub 🚀")

def suma(a, b):
    return a + b

if __name__ == "__main__":
    nombre = input("¿Cuál es tu nombre? ")
    saludar(nombre)

    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa otro número: "))

    resultado = suma(num1, num2)
    print(f"La suma es: {resultado}")