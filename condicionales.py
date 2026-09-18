#EJERCICIOS EN CLASE
#Ejercicio de ejemplo

# Ejercicio 1: Determinar si un número es positivo, negativo o cero
numero = float(input("Ingrese un número: "))

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print("El número es cero")

# Ejercicio 2: Verificar si una persona es mayor de edad
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Ejercicio 3: Determinar si un número es par o impar
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:      # si el residuo es 0 → es par
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

# Ejercicio 4: Clasificar una nota académica
nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))

if nota >= 4.5:
    print("Desempeño superior")
elif nota >= 3.5:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
else:
    print("Desempeño bajo")

# Ejercicio 5: Determinar el mayor de tres números
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

print(f"El mayor de los tres números es: {mayor}")

#TALLER
#Punto 1: Determinar mayor o menor de edad
#Crear Variables
print("Por favor ingrese los siguientes datos\n")

var_nombre = input("Nombre: ")
var_edad = int(input("Edad: "))

#Crear condicion
if var_edad < 0 :
    print("¡ERROR! Valor incorrecto")
elif var_edad >= 18 :
    print(f"{var_nombre} Eres mayor de edad")
else:
    faltante = 18 - var_edad
    print(f"{var_nombre} Eres menor de edad y te faltan {faltante} años")

#Punto 2: Nota Final
print("Ejercicio: Nota Final")

var_nombre = input(f"Nombre: ")
var_notafinal = float(input("Nota Final: "))

if var_notafinal <0 or var_notafinal > 5.0 :
    print(f"Nota invalida")
elif var_notafinal >= 3.0 and var_notafinal <= 3.4 :
    print(f"Estudiante {var_nombre} con nota: {var_notafinal}, GANO 🎉 con un desempeño ACEPTABLE")
elif var_notafinal >= 3.5 and var_notafinal <= 4.4 :
    print(f"Estudiante {var_nombre} con nota: {var_notafinal}, GANO 🎉 con un desempeño BUENO")
elif var_notafinal >= 4.5 and var_notafinal <= 5.0 :
    print(f"Estudiante {var_nombre} con nota: {var_notafinal}, GANO 🎉 con un desempeño EXCELENTE")
else:
    print(f"Estudiante {var_nombre} con nota: {var_notafinal}, PERDIO ❌ con un desempeño INSUFICIENTE")


#Punto 3: Descuento a cliente
print("Ejercicio: Descuento")

var_nombre = input("Nombre: ")
var_valorcompra = float(input("Valor de compra: "))

if var_valorcompra <= 0 :
    print("¡ERROR! Valor no valido")
elif var_valorcompra > 0 and var_valorcompra < 100000 :
    print(f"""
    -Cliente: {var_nombre}
    -Compra {var_valorcompra} no se aplica descuento
    """)
elif var_valorcompra >= 100000 and var_valorcompra < 300000 :
    var_descuento = var_valorcompra * 0.1
    var_totalpagar = var_valorcompra - var_descuento
    print(f"""
    -Cliente {var_nombre}
    -Compra de {var_descuento}
    -Descuento del 10% {var_descuento}
    -Total a pagar es: {int(var_totalpagar)}
    """)
elif var_valorcompra >= 300000 and var_valorcompra < 500000 :
    var_descuento = var_valorcompra * 0.15
    var_totalpagar = var_valorcompra - var_descuento
    print(f"""
    -Cliente {var_nombre}
    -Compra de {var_descuento}
    -Descuento del 15% {var_descuento}
    -Total a pagar es: {int(var_totalpagar)}
    """)
else:
    var_descuento = var_valorcompra * 0.2
    var_totalpagar = var_valorcompra - var_descuento
    print(f"""
    -Cliente {var_nombre}
    -Compra de {var_descuento}
    -Descuento del 10% {var_descuento}
    -Total a pagar es: {int(var_totalpagar)}
    """)

#Punto 4: Temperaturas
print("Ejercicio: Temperatura")

ciudad = input("Ingrese el nombre de la ciudad: ")
temperatura = float(input("Ingrese la temperatura actual en °C: "))

if temperatura < 10:
    clasificacion = "Muy fría"
elif temperatura >= 10 and temperatura <= 17:
    clasificacion = "Fría"
elif temperatura >= 18 and temperatura <= 25:
    clasificacion = "Templada"
elif temperatura >= 26 and temperatura <= 32:
    clasificacion = "Caliente"
else:
    clasificacion = "Muy caliente"

if temperatura < 18:
    recomendacion = "Se recomienda llevar abrigo."
else:
    recomendacion = "No es necesario llevar abrigo."

print(f"""
-Ciudad: {ciudad}
-Temperatura: {temperatura} °C
-Clasificación: {clasificacion}
-Recomendación: {recomendacion}
""")

#Punto 5:Nomina
print("Ejercicio: Valor horas")
nombre = input("Ingrese el nombre del empleado: ")

horas = float(input("Ingrese las horas trabajadas durante el mes: "))
valor_hora = float(input("Ingrese el valor de la hora normal: "))

if horas <= 0 or valor_hora <= 0:
    print("Error: las horas trabajadas y el valor de la hora deben ser positivos.")
else:
    if horas <= 160:
        horas_normales = horas
        horas_extra = 0
    else:
        horas_normales = 160
        horas_extra = horas - 160

    pago_horas_normales = horas_normales * valor_hora
    valor_hora_extra = valor_hora * 1.25
    pago_horas_extra = horas_extra * valor_hora_extra

    salario_bruto = pago_horas_normales + pago_horas_extra

    descuento = salario_bruto * 0.08

    salario_neto = salario_bruto - descuento

    print(f"""
    -Empleado: {nombre}
    -Horas normales: {horas_normales}
    -Horas extra: {horas_extra}
    -Pago por hora normal: {valor_hora}
    -Pago por hora extra: {valor_hora_extra}
    -Salario total (bruto): {salario_bruto}
    -Descuento de salud y pensión (8%): {descuento}
    -Salario neto: {salario_neto}
    """)
