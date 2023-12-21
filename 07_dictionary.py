# Dict


my_dict = dict()
my_other_dict = ()
print(type(my_dict))


my_other_dict = {"nombre": "ceasr",
                 "apellido": "bravo", "Edad": 35, 1: "Python"}

print(my_other_dict)

my_dict = {"nombre": "ceasr",
           "apellido": "bravo", "Edad": 35, "lenguajes": {"Python", "Swift", "C#"}, "altura": "1.82"}

print(my_dict)

print(len(my_dict))


print(my_dict["nombre"])
my_dict["Nombre"] = "Pedro"
print(my_dict["nombre"])

# dice falso aunque esta en el diccionario,esta buscando por clave no por valor
print("ceasr" in my_dict)
# dice falso aunque esta en el diccionario,esta buscando por clave no por valor
print("apellido" in my_dict)
# como se puede buscar por valor?
print("--------------------------------------")
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys("nombre", 4))
print("--------------------------------------")

my_new_dict = dict.fromkeys(("nombre", 1, "piso"))    # diccionario vacio
print(my_new_dict)
my_new_dict = dict.fromkeys(("nombre", 1, "piso"))    # diccionario vacio
my_new_dict = dict.fromkeys(("nombre", 1, "piso"))    # diccionario vacio
print("--------------------------------------")

print(list(my_dict.values()7))
