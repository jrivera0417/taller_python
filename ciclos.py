#EJERCICIOS EN CLASE
#Ejercicio de ejemplo
'''
# Ejercicio 1: Mostrar la tabla de multiplicar de un número
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):          # recorre los valores del 1 al 10
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 2: Sumar los primeros n números naturales
n = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma = suma + i

print(f"La suma de los primeros {n} números naturales es: {suma}")

# Ejercicio 3: Contar cuántos números pares hay entre 1 y n
n = int(input("Ingrese un número entero positivo: "))

contador = 0
numero   = 1
while numero <= n:
    if numero % 2 == 0:
        contador = contador + 1
    numero = numero + 1

print(f"Hay {contador} números pares entre 1 y {n}")

# Ejercicio 4: Solicitar una contraseña hasta que sea correcta
clave_correcta  = "python2026"
clave_ingresada = input("Ingrese la contraseña: ")

while clave_ingresada != clave_correcta:
    print("Contraseña incorrecta, intente de nuevo")
    clave_ingresada = input("Ingrese la contraseña: ")

print("Contraseña correcta, acceso concedido")

# Ejercicio 5: Calcular el factorial de un número
n = int(input("Ingrese un número entero no negativo: "))

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f"El factorial de {n} es: {factorial}")

#TALLER
#Punto 1: Adivinar el número
import random

numero_secreto = random.randint(1, 10)

while True:
    intento = int(input("Adivina el número (entre 1 y 10): "))

    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        break
    else:
        print("Incorrecto. Intenta nuevamente.")

#Punto 2: Cuenta regresiva
numero = int(input("Ingresa un número entero mayor que 0: "))

while numero >= 0:
    print(numero)
    numero = numero - 1

print("¡Cuenta regresiva terminada!")

#Punto 3: Identificar números impares
for numero in range(1, 101):
    if numero % 2 != 0:
        print(numero)

#Punto 4: Menú interactivo
from datetime import datetime

while True:
    print("""     --- MENÚ PRINCIPAL ---
    1. Mensaje de bienvenida
    2. Fecha y hora actual
    3. Salir""")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("¡Bienvenido al programa!")

    elif opcion == "2":
        fecha_hora = datetime.now()
        print("Fecha y hora actual:", fecha_hora)

    elif opcion == "3":
        print("¡Programa finalizado!")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")
'''
#Punto 5: Registro de notas y calculo de promedio
estudiante = input("Ingresa el nombre del estudiante: ")
cantidad = int(input("¿Cuántas notas deseas registrar?: "))

suma = 0
notas_registradas = 0

for i in range(cantidad):

    nota = float(input(f"Ingresa la nota {i + 1} (0 a 5): "))

    if nota < 0 or nota > 5:
        print("""❌ Error: la nota debe estar entre 0 y 5.
        El registro de notas ha terminado.""")
        exit()

    suma += nota
    notas_registradas = notas_registradas + 1

if notas_registradas > 0:

    promedio = suma / notas_registradas

    if promedio >= 3.5:
        print(f"El estudiante {estudiante} aprobó con un promedio de: {promedio:.2f}. 🎉🎉🎉")
    else:
        print(f"El estudiante {estudiante} no aprobó con un promedio de: {promedio:.2f}. ❌")

else:
    print("No se registraron notas válidas.")
