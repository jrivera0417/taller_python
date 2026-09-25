#Repaso Ciclos.
'''
lista_producto = [] #Lista en blanco
cantidad = int(input("Cantidad de productos a comprar: "))

for i in range(cantidad):
    producto = input(f"Nombre del producto {i+1}: ")
    #Agregar producto a lista
    #.append guarda lo que este en la variable
    lista_producto.append(producto)
print(f"Productos comprados: {lista_producto}")
'''
lista_firulais = []
lista_michis = []

while True:
    pregunta = int(input("""
    1. Registrar Firulais 🐶
    2. Registrar Michis 😺
    3. Listado de Firulais 🐕
    4. Listado de Michis 🐈
    5. Salir
    """))

    if pregunta == 1:
        nombre_firulais = input("Nombre del Perro 🦴: ")
        lista_firulais.append(nombre_firulais)
        print("Firulais registrado")
    elif pregunta == 2:
        nombre_michi = input("Nombre del Gato 😸: ")
        lista_michis.append(nombre_michi)
        print("Michi registrado")
    elif pregunta == 3:
        print(f"Los Firulais registrados son: {lista_firulais}")
    elif pregunta == 4:
        print(f"Los Michis registrados son: {lista_michis}")
    elif pregunta == 5:
        print("Saliendo del sistema")
        break
    else:
        print("Opción Invalida")