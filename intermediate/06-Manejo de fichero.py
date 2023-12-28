# manejo de ficheros

import json
import os

txt_file = open("./my_file.txt", "r+")  # leer y escribit
# print(txt_file.read(10))

# print(txt_file.)
# print(txt_file.readlines())             # return a list.


for line in txt_file.readlines():
    print(line)


txt_file.write("\n Aunque tambien me gusta C++  \n")   # append to the file
txt_file.close()

# os.remove("./my_file")


json_file = open("./my_file.json", "w+")

json_test = {
    "name": "Brais",
    "surname": "bravo",
    "age": "35 años",
    "lenguajes": ["pryhon", "c++"]

}

json.dump(json_test, json_file, indent=3)

json_file.close()

json_dict = json.load(open("./my_file.json"))

print(json_dict)
print(type(json_dict))
print(json_dict["name"], json_dict["age"])
