##### tuples ######

my_tuple = tuple()
my_other_ruple = ()

my_tuple = (35, 1.77, "cesar", "bravo")
my_other_tuple = (10, 12, 24, 100)

print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[3])
print(my_tuple[2])
print(len(my_tuple))

print(my_tuple[int(len(my_tuple)-1)])

print(my_tuple.count(35))  # 0 -> no hay elemento en la lista
print(my_tuple.index(35))    # devuleve la posciion
print("------")
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[1] = "bravo del alamo"
my_tuple.insert(1, "azul")
print(my_tuple)
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))



==
