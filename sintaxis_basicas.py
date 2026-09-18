# Creacion de Variables

nombre = 'Alexis' #Variable tipo String (Texto)
documento = 1000 #Variable tipo Int (Entero)
direccion = 'Medellín Crr 118' #Variable de tipo string (cadena de texto)
tiene_deudas = True #Variable tipo bool (booleano)

#MOSTRAR EL CONTENIDO DE UNA VARIABLE EN PANTALLA
print(nombre)

#CONCATENACIÓN USANDO +
print('CONCATENACIÓN USANDO +')
print('=' * 30)
#Opcion 1: Usando + NO RECOMENDADA
print("Mi nombre es: " + nombre + " y mi documento es: " + str(documento))

#CONCATENACIÓN USANDO ,
print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)
#Opcion 2: Usando , RECOMENDADA
print("Mi nombre es:", nombre, "y mi documento es:", documento, "mi dirección es: ", direccion, "Tienes deudas?: ", tiene_deudas)

#CONCATENACIÓN USANDO F-STRINGS
print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)
#Opcion 3: RECOMEDADA POR LA DOCENTE
print(f"Mi nombre es: {nombre} y mi documento es: {documento} mi dirección es: {direccion} tienes deudas?: {tiene_deudas}")

# F-STRINGS CON VARIAS VARIABLES
print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)

# Opcion 4
print(f"""
Nombre:         {nombre}
Documento:      {documento}
Dirección:      {direccion}
¿Tiene deudas?: {tiene_deudas}
""")

# SALTO DE LÍNEA EN PYTHON
# Salto de línea al inicio del texto
print(f"\n Hola, {nombre}!")
# Salto de línea al final del texto
print(f"Bienvenida {nombre} a Python.\n")