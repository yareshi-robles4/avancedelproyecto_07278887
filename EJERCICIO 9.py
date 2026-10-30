print("\n*** Yareshi 1:   07278887:   ***")
print("*** Hanani 2:    07308762:   ***\n")

print("*** Ejercicio 9 Tamaño de tu bebida ***")

#Mostramos el menu para que el usuario sepa que puede elegir
print("\n===== MENU DE TAMAÑOS =====")
print("1 = Chico   ($55)")
print("2 = Mediano ($70)")
print("3 = Grande  ($85)")

#input() pregunta y guarda la respuesta como TEXTO
#int() la convierte a numero entero para poder comprarla con 1, 2 y 3
opcion = int(input("\n¿Que tamaño quieres? Escribe 1, 2 y 3: "))
#Si el usuario escribe 2, ahora opcion vale 2

#PREGUNTA 1: ¿2 es igual a 1? Respuesta: False, entonces pasa a la siguiente pregunta
if opcion == 1:
    print("Elegiste tamaño CHICO, son $55")

    #PREGUNTA 2: ¿2 es igual a 2? Respuesta: True, entonces muestra este mensaje
    #y Python YA NO revisa las preguntas de abajo
elif opcion == 2:
    print("Elegiste tamaño MEDIANO, son $70")

    #PREGUNTA 3: solo se revisa si las dos anteriores fueron false
elif opcion == 3:
    print("Elegiste tamaño GRANDE, son $85")

    #else: entra aqui solo si NINGUNA pregunta fue true, (escribio 4, 7, 8, etc.)
else:
    print("Opcion no valida, elige 1, 2 o 3")

#Esta linea no tiene sangria, no pertenece al if, por eso se muestra siempre
print("\n¡Gracias por tu compra!")