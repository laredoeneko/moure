# funciones con funciones
#   funciones anidadas, f


from functools import reduce


def sum_one(value):
    return value+1


def sum_five(value):
    return value+5


def sum_two_values_and_one(first_Value, second_value, sum_one):
    return sum_one(first_Value + second_value)


def sum_two_values_and_add_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


# se pasa como parametro una funcion
print(sum_two_values_and_one(5, 2, sum_one))
# se pasa como parametro la segunda funcion
print(sum_two_values_and_one(5, 2, sum_five))


# Closures

# funciones que devuelve funciones

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_clousere = sum_ten(1)
print(add_clousere(5))

print(sum_ten(5)(1))


##### Builtin higher order functions   3#####

numbers = [2, 5, 20, 21]


def multiply_two(number):
    return number*2


print(list(map(multiply_two, numbers)))
# hay que convertirlo en lista, ha aplicado sobre cada valor de las lista la operacion de la function

print(list(map(lambda number: number*2, numbers)))
# hay que convertirlo en lista, ha aplicado sobre cada valor de las lista la operacion de la function2

# Filter
#


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


# devilve los valores mayoures de 20
print(list(filter(filter_greater_than_ten, numbers)))

print(list(filter(lambda number: number > 10, numbers)))


# reduce valor mas el acumulado

print("--------------------------")


def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value+second_value


# no da como resultado una lista, solo un valor, la suma de los dos ultimos valores de la lista
reduce(sum_two_values, numbers)

print(reduce(sum_two_values, numbers))
