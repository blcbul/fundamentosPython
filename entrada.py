# function input -> retorna string

num_a = int(input("Ingresa un numero: "))
num_b = int(input("Ingresa un numero: "))

print(num_a + num_b)

name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))
city = input("Inbgresa tu ciudad/pueblo: ")

# strimg format
"""
Hola,soy name,tengo age años y vivo en city
"""

greeting = "Hola, soy {}, tengo {} años y vivo en {}"

print(greeting.format(name, age, city))

greeting_2 = f"Hola, soy {name}, tengo {age} años y vivo en {city}"
print(greeting_2)