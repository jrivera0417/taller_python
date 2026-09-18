# ============================================================
# OPERADORES ARITMÉTICOS EN PYTHON
# ============================================================
numero1 = 10
numero2 = 3

suma           = numero1 + numero2   # 13
resta          = numero1 - numero2   # 7
multiplicacion = numero1 * numero2   # 30
division       = numero1 / numero2   # 3.333...
division_entera= numero1 // numero2  # 3
residuo        = numero1 % numero2   # 1
potencia       = numero1 ** numero2  # 1000

print(f"""
Resultado de Operaciones Aritméticas:
Suma:            {numero1} +  {numero2} = {suma}
Resta:           {numero1} -  {numero2} = {resta}
Multiplicacion:  {numero1} *  {numero2} = {multiplicacion}
Division:        {numero1} /  {numero2} = {division:.4f}
Division entera: {numero1} // {numero2} = {division_entera}
Residuo:         {numero1} %  {numero2} = {residuo}
Potencia:        {numero1} ** {numero2} = {potencia}
""")