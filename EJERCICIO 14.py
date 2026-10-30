print("\n*** Yareshi 1:   07278887:        ***")
print("*** Hanani 2: 07308762:           ***\n")

print("*** Ejercicio 14 Costo de envio ***")

#float() convierte a numero con decimales, porque el dinero y los km pueden tener decimales
pedido = float(input("\n¿Cuanto es tu pedido? $"))
#Si el usuario escribe 250, ahora pedido vale 250.0
distancia = float(input("¿A cuantos km vives de la tienda? "))
#Si el usuario escribe 8, ahora distancia vale 8.0

#En cada opcion GUARDAMOS el costo de envio en la misma variable
#¿8.0 es menor o igual que 3? False, pasa a la siguiente
if distancia < 3:
    costo_envio = 0
    print("\n¡Envio gratis!")

#¿8.0 es menor o igual que 10? True, guarda 39 y TERMINA
elif distancia < 10:
    costo_envio = 39
    print("\nEl envio cuesta $39")

elif distancia < 20:
    costo_envio = 69
    print("\nEl envio cuesta $69")

#else: vive a mas de 20 km
else:
    costo_envio = 0
    print("\nNo hacemos envios a mas de 20 km, recoge tu pedido en tienda")

#Esta parte no tiene sangria, se hace SIEMPRE
#Ahora costo_envio vale 39, esta formula dice: total = 250.0 + 39
total = pedido + costo_envio
print(f"Pedido: ${pedido:.2f}")
print(f"Envio: ${costo_envio:.2f}")
print(f"TOTAL A PAGAR: ${total:.2f}")