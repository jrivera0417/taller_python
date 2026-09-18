#EJERCICIOS EN CLASE
# Ejercicio 1: Suma de dos números
print("Ejercicio 1: Suma de dos números")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2   # Se calcula la suma

print(f"La suma es: {suma}")
print("-" * 50)

# Ejercicio 2: Área de un rectángulo
print("Ejercicio 2: Área de un rectángulo")
base   = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

area = base * altura   # fórmula: base × altura

print(f"El área del rectángulo es: {area}")
print("-" * 50)

# Ejercicio 3: Conversión de minutos a horas y minutos
print("Ejercicio 3: Conversión de minutos a horas y minutos")
minutos_totales = int(input("Ingrese la cantidad de minutos: "))

horas   = minutos_totales // 60   # división entera → horas completas
minutos = minutos_totales % 60    # módulo → minutos restantes

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")
print("-" * 50)

# Ejercicio 4: Cálculo del precio con descuento
print("Ejercicio 4: Cálculo del precio con descuento")
precio    = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento / 100)   # valor que se descuenta
precio_final    = precio - valor_descuento      # precio con descuento

print(f"El precio final a pagar es: {precio_final}")
print("-" * 50)

# Ejercicio 5: Intercambio de valores entre dos variables
print("Ejercicio 5: Intercambio de valores entre dos variables")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

auxiliar = a   # guardar temporalmente el valor de a
a = b          # a toma el valor de b
b = auxiliar   # b toma el valor original de a

print(f"Después del intercambio: a = {a} , b = {b}")
print("-" * 50)

#TALLER
#Punto 1: Calcular perímetro
print("Punto 1: Calcular perímetro")

largo = float(input("Ingrese el largo del terreno: "))
ancho = float(input("Ingrese el ancho del terreno: "))

perimetro = largo * 2 + ancho * 2

print(f"El perímetro del terreno es de: {perimetro}")
print("=" * 60)

#Punto 2: Promedio de tres números
print("Punto 2: Promedio de tres números")

a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))
c = float(input("Ingrese el tercer valor: "))

promedio = (a + b + c) / 3

print(f"El promedio de los valores {a}, {b}, {c} es de: {promedio:.4f}")
print("=" * 60)

#Punto 3: Mensaje de presentación
print("Punto 3: Mensaje de presentación")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print(f"Hola, mi nombre es {nombre} y tengo {edad} años")
print("=" * 60)

#Punto 4: Conversión de peso colombiano a dólar
print("Punto 4: Conversión de peso colombiano a dólar")

pesos = float(input("Ingrese el total de pesos colombianos(COP) a convertir: "))
tasa_fija = 4000

cambio = pesos / tasa_fija

print(f"La cantidad total en dólares(USD) es de: {cambio}")
print("=" * 60)

#Punto 5: Pasar segundos a minutos y segundos
print("Punto 5: Pasar segundos a minutos y segundos")
segundos_totales = int(input("Ingrese la cantidad de segundos: "))

segundos = segundos_totales % 60
minutos = segundos_totales // 60
horas = segundos_totales // 3600

print(f"{segundos_totales} segundos equivalen a {horas} horas, {minutos} minutos y {segundos} segundos")
print("-" * 60)