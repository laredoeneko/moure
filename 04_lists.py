my_list = [1, 2, 3, 4, 5]

print(my_list)
print(my_list[1])

print(my_list[-1])

my_other_list = my_list
my_other_list.append("bravo")
my_other_list.insert(0, "Azul")
print(my_other_list)

my_other_list.remove("bravo")
print("_----------")
print(my_other_list)
my_pop_element = my_other_list.pop()   # guardo el elemento de la lista
print(my_pop_element)
print(my_other_list)
my_other_list.pop()


print(my_other_list)
my_list_2 = my_list.copy()
my_other_list.clear()
print(my_other_list)
print("_----------")

print(my_list_2)
my_list_2.reverse()
print(my_list_2)
print(my_list[1:2])
