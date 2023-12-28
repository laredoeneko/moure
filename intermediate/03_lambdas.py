##### Funciones lambdas ###########


two_values = lambda first_value, second_value: first_value*second_value



print(two_values(234345, 4))

div_values = lambda first_value, second_value: first_value*second_value -3 

print(div_values(2,4))

def three_values(first_value):
   return lambda first_value, second_value: first_value+second_value+ value

print(three_values(5)(2,4) )
