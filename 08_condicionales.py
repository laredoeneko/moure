####### Condicionales ######

my_condition = True

if my_condition == True:
    print("Se ejecuta la condicion de if")

my_condition = 5 * 2

if my_condition == 10:    #
    print("Se ejecuta la condicion del segundo if")

if my_condition >= 10:
    print("se ejecuta la tercera condicion")

if my_condition >= 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")

print("La ejecucion continua")
print("---------------------------------------------------")
my_condition = 22

if my_condition >= 10 and my_condition < 20:
    print("Es mayor que 10")
elif my_condition < 10:
    print("menor de 10")
elif my_condition > 20:
    print("mayor de 20")
else:
    print("esta entre 10 y 20")

print("La ejecucion continua")

print("---------------------------------------------------")
my_string = "cesar"
if my_string == "cesar":
    print("la cadena coincide")
print("---------------------------------------------------")


my_string = "a"
if not my_string:
    print("mi cadena de texto esta vacia")
else:
    print("cadena no vacia")
