print("\n*** Yareshi 1: Matricula: 07278887       ***")
print("*** Hanani 2: Matricula: 07308762        ***\n")

print("*** Ejercicio 4 MI META DE AHORRO   ***")

producto = input("¿Que quieres comprar? ")
precio = float(input("¿Cuanto cuestan? "))
ahorrado = float(input("¿Cuanto tienes ahorrado? "))
ahorro_semanal = float(input("¿Cuanto ahorras por semana? "))

if ahorrado >= precio:
    print("¡Ya puedes comprar tus", producto + "!")
else:
    faltantes = precio - ahorrado
    semanas = faltantes / ahorro_semanal
    print("Te faltan $",  faltantes, " para tus", producto, sep="")
    print("Ahorrando $", ahorro_semanal, " por semanal, los tendras en ", semanas, " semanas", sep="")
    print("\n")