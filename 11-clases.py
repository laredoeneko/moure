##### clasess ####

class MyPerson:
    pass


print(MyPerson)


class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname


my_person = Person("cesar", "bravo")
print(my_person.name)
print(f"{my_person.surname}      {my_person.name}")

print("clases definida de otra manera ")


class Person:
    def __init__(self, name, surname, alias="sin alias") -> None:
        self.full_name = f'{surname}      {name}  {alias}'

    def walk(self):
        print(f"{self.full_name}\nEsta caminando")


my_person = Person("cesar", "bravo")
print(my_person.full_name)
my_person.walk()


my_other_person = Person("brais", "moure", "moureDev")

my_other_person.walk()
