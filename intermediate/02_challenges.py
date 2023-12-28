##### challanges  ###########

##### challanges  ###########
# Escribe un programa que muestre por consola (con un print) los
# * números de 1 a 100 (ambos incluidos y con un salto de línea entre
# * cada impresión), sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
# */

def fizzbuzz():
    for element in range(3, 101):

        if element % 3 == 0 and element % 5 == 0:
            print(element, "fizzbuzz")
        elif element % 3 == 0:
            print(element, "fizz")
        elif element % 5 == 0:
            print(element, "buzz")

# fizzbuzz()


# comprobar si es un anagrama.
# palabras que tienen las mismas letras


def is_anagrama(first_word, second_word):
    if first_word.lower() == second_word.lower():
        return "no es un anagrama"
    print(sorted(first_word))
    print(sorted(second_word))
    return sorted(first_word.lower()) == sorted(second_word.lower())


if (is_anagrama("amor", "romas") == True):
    print(" es un anagrama")
else:
    print("no es un anagrama")


#  sucesion de fibonacci
# el siguiente numero es la suma del anterior
#

def fibonacci():

    prev = 0
    next = 1
    for element in range(0, 50):
        print(prev)
        fib = prev+next
        prev = next
        next = fib


fibonacci()


# otro ejercicio
# calculo de numero primo

def is_prime():

    for number in range(1, 101):

        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)


print("---------------------------")

is_prime()
print("---------------------------")


# pasamos una cadena de texto y la escribimos al reves.


def al_reves(name):
    print(name)
    reversed_text = ""
    text_len = len(name)

    for a in range(0, len(name)):
        reversed_text += name[text_len-a-1]
    return reversed_text


print(al_reves("hola mundo"))
