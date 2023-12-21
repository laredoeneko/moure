###### excepciones manejo de errores  ######


numberOne = 5
numberTwo = 1
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")

except:
    print("se ha producido un error")

else:    # se ejecuta si no hay error
    print("la ejecucion continua correctamente ")

finally:   # se ejecuta siempre
    print("la ejecucion continua")

numberOne = 5
numberTwo = "1"

print(numberOne+numberTwo)
# captura de excepciones por tipo.

try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except ValueError as e:    # solo si se product un ValueError
    print("se ha producido un error")
except TypeError:    # solo si se product un typeError
    print("se ha producido un error")
