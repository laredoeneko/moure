# sets ##### elementos no ordenador y no repetidos
# array con elementos no ordenados y no repetidos
# tuplas no se pueden modificar los set SI. No es una estructura ordenada


my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"cesar", "bravo", 49, "del",
                "alamo", "aalamo", 1, 2, 1, 1, 1, 1, 1, 1}

print(my_other_set)
print(">> ", len(my_other_set))
print(my_other_set.add("agustin"))
print(">> ", my_other_set)

print("cesar" in my_other_set)
print("cesare" in my_other_set)
