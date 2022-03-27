from typing import ForwardRef


for i in range(5):
    nombre = input("ingrese nombre del comprador: ")
    apellido = input("ingrese apellido del comprador: ")
    marca = input("ingrese marca: ")
    if marca == "Ford":
        precio_marca = 10000
    elif marca == "fiat":
        precio_marca = 15000
    elif marca == "chevrolet":
        precio_marca = 20000
    puertas = input("ingrese numero de puertas: ")
    if puertas == "3":
        precio_puertas = 50000
    elif puertas == "4":
        precio_puertas = 60000
    elif puertas == "5":
        precio_puertas = 70000
    color = input("ingrese color: ")
    if color == "blanco":
        precio_color = 10000
    elif color == "negro":
        precio_color = 20000
    elif color == "azul":
        precio_color = 30000
    precio_final = precio_marca+precio_color+precio_puertas
    
    print("la persona :"+nombre+" "+apellido+" compro un auto marca "+marca+" de "+puertas+" puertas y color "+color+" con un precio final de pesos "str(precio_final))
                                                                                                                                                
    
        