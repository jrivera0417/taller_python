#Repaso Variables y condicionales
#Variables
print("=== Tienda donde Ely ===")

print("Por favor ingrese la siguiente información: \n")
cliente = input("Nombre de cliente: ")
producto = input("Nombre de producto: ")
cantidad = int(input("Cantidad: "))
precio = float(input("Prseio: $ "))

#Variable para preguntar si es a domicilio
domicilio = input("La compra es para domicilio (SI - NO): ")

#Condicional verificar que respondio el usuario
#.upper() convierte en mayuscula .lower minuscula
if domicilio.upper() == "NO":
    print("=== RESUMEN DE COMPRA ===")
    print(f"""
    - Cliente: {cliente}
    - Producto: {producto}
    - Cantidad: {cantidad}
    - Precio: $ {precio}
    - Total a pagar: $ {cantidad * precio}

    GRACIAS POR TU COMPRA 🛒🛒
    """)
elif domicilio.upper() == "SI":
    direccion = input("Ingrese municipio de envio (Medellín, Itagüí, Bello): ")

    valor_domicilio = 0
    if direccion.lower() == "medellin":
        valor_domicilio = 5000
    elif direccion.lower() == "itagui":
        valor_domicilio = 10000
    elif direccion.lower() == "bello":
        valor_domicilio = 8000
    else:
        print("Municipio Invalido")

    valor_compra = (cantidad * precio) + valor_domicilio

    print("=== RESUMEN DE COMPRA ===")
    print(f"""
        - Cliente: {cliente}
        - Producto: {producto}
        - Cantidad: {cantidad}
        - Precio: $ {precio}
        - Subtotal: $ {cantidad * precio}
        - Valor domicilio: $ {valor_domicilio}
        - Total a pagar: $ {valor_compra}
    
        GRACIAS POR TU COMPRA 🛒🛒
        """)
else:
    print("Opción Invalida")