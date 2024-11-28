# Python Learning Summary
"""python --version
py --list
where python
PS Get-Command python

python -m venv venv
PS .\venv\Scripts\Activate
cmd .\venv\Scripts\activate
pip install numpy scipy matplotlib
py -3.12 -m venv .venv ou /path/to/python3.12 -m venv .venv
dir(comando) Use to list all methods of a command
*in import does not need to declare the class. and . indicates the base folder of the project, .. returns 2 directories.
The __init__.py file transforms a directory into a Python package, allowing the contents of that directory to be imported into other modules.
relative import
prospector
"""
import time


start = time.time()
_spaces_ = 10

# ------------------------1- Data Types in Python--------------------------------------
print(" " * _spaces_ + "1- Data Types in Python")

# Integer (int)
integer_variable = 42
print("Integer (int):", integer_variable)

# Float (float)
float_variable = 3.14159
print("Float (float):", float_variable)

# Boolean (bool)
bool_variable = True
print("Boolean (bool):", bool_variable)

# String (str)
string_variable = "Hello, Python!"
print("String (str):", string_variable)

# NoneType (None)
none_variable = None
print("NoneType (None):", none_variable)

# Complex Numbers (complex)
complex_variable = 2 + 3j
print("Complex (complex):", complex_variable)

# List
list_variable = [1, 2, 3, 4, 5]
print("List:", list_variable)

# Tuple
tuple_variable = (10, 20, 30)
print("Tuple:", tuple_variable)

# Set
set_variable = {10, 20, 30, 30}  # Duplicates are removed
print("Set:", set_variable)

# Dictionary
dict_variable = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", dict_variable)

# Bytes
bytes_variable = b"Byte string"
print("Bytes:", bytes_variable)

# Bytearray
bytearray_variable = bytearray([65, 66, 67])
print("Bytearray:", bytearray_variable)

# MemoryView
memory_view_variable = memoryview(bytearray_variable)
print("MemoryView:", memory_view_variable)

# Type Checking
print("Type of integer_variable:", type(integer_variable))
print("Type of float_variable:", type(float_variable))

# Dynamic Typing
dynamic_variable = 42  # Initially an int
print("Dynamic Typing Example (int):", dynamic_variable)
dynamic_variable = "Now I'm a string"  # Changed to a string
print("Dynamic Typing Example (str):", dynamic_variable)

# ------------------------2- Args and Kwargs--------------------------------------
print(" " * _spaces_ + "2- Args and Kwargs")

def calcular_imposto_args(valor, *args):
    total_imposto = 0
    for item in args:
        total_imposto += valor * item
    return total_imposto

print("Using *args:", calcular_imposto_args(1000, 0.275, 0.05, 0.0375, 0.03))

def calcular_imposto_trimestral(valor, **kwargs):
    total_imposto = 0
    if "perc_ir" in kwargs:
        total_imposto += valor * kwargs["perc_ir"]
    if "perc_csll" in kwargs:
        total_imposto += valor * kwargs["perc_csll"]
    return total_imposto

print(
    "Using **kwargs:",
    calcular_imposto_trimestral(1000, perc_ir=0.275, perc_csll=0.09325),
)

# ------------------------3- If __name__ == "__main__"--------------------------------------
print(" " * _spaces_ + "3- If __name__ == '__main__'")

def calcular_imposto(faturamento):
    if faturamento < 1666:
        taxa = 6
    elif faturamento < 16666:
        taxa = 6.1
    elif faturamento < 566666:
        taxa = 6.15
    else:
        taxa = 6.2
    imposto = taxa * faturamento
    print(imposto)
    return imposto

if __name__ == "__main__":
    calcular_imposto(1666)

# ------------------------4- Underline or Underscore--------------------------------------
print(" " * _spaces_ + "4- Underline or Underscore")

faturamento = 1_000_000_000  # This line is equivalent to 1000000000
print(f"Formatted number with underscores: {faturamento}")

def calcular_imposto(faturamento):
    if faturamento < 1666:
        taxa = 6
    elif faturamento < 16666:
        taxa = 6.1
    elif faturamento < 566666:
        taxa = 6.15
    else:
        taxa = 6.2
    isento_imposto = taxa == 6
    imposto = taxa * faturamento
    return imposto, isento_imposto

faturamento = 15666
valor_imposto, _ = calcular_imposto(faturamento)  # Using underscore to ignore variable
lucro = faturamento - valor_imposto
print(f"Lucro: {lucro}")

# ------------------------5- Type Hints--------------------------------------
print(" " * _spaces_ + "5- Type Hints")

def calcular_taxa(faturamento: float) -> float:
    if faturamento < 1666:
        taxa = 6
    elif faturamento < 16666:
        taxa = 6.1
    elif faturamento < 566666:
        taxa = 6.15
    else:
        taxa = 6.2
    return taxa

def calcular_imposto(faturamento: float) -> None:
    taxa = calcular_taxa(faturamento)
    imposto = taxa * faturamento
    print(imposto)

if __name__ == "__main__":
    calcular_imposto(200)

# ------------------------- Other Sections--------------------------------------
# The rest of the code remains the same, with sections on:
# - List Comprehensions
# - Map, Filter, and Reduce
# - Exception Handling
# - Context Managers
# - Decorators
# - Generators
# - Environment Variables
# - Python Modules and Imports
# - F-strings
# - Data Structures (Dicts, Sets, Tuples)



# ------------------------6- List Comprehension--------------------------------------
print(" " * _spaces_ + "6- List Comprehension")

faturamentos = [18, 15, 36, 46, 76]
impostos = [0.5 * f for f in faturamentos]
print("List comprehension results:", impostos)

# ------------------------7- Map, Filter, Reduce--------------------------------------
print(" " * _spaces_ + "7- Map, Filter, Reduce")

from functools import reduce

# Map
precos_produtos = [5000, 9000, 2000, 15000]
def aplicar_aumento(preco):
    return preco * 1.1 if preco > 6666 else preco

precos_grodutos = list(map(aplicar_aumento, precos_produtos))
print("Map results:", precos_grodutos)

# Filter
def preco_maior_que_6000(preco):
    return preco > 6000

precos_filtrados = list(filter(preco_maior_que_6000, precos_produtos))
print("Filter results:", precos_filtrados)

# Reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print("Reduce results:", product)

# ------------------------8- Exception Handling--------------------------------------
print(" " * _spaces_ + "8- Exception Handling")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Exception caught:", e)

# ------------------------9- Context Managers--------------------------------------
print(" " * _spaces_ + "9- Context Managers")

with open("example.txt", "w") as file:
    file.write("Hello, World!")

# ------------------------10- Decorators--------------------------------------
print(" " * _spaces_ + "10- Decorators")

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# ------------------------11- Generators--------------------------------------
print(" " * _spaces_ + "11- Generators")

def generate_numbers():
    for i in range(5):
        yield i

for num in generate_numbers():
    print("Generator:", num)

# ------------------------12- Environment Variables--------------------------------------
print(" " * _spaces_ + "12- Environment Variables")

from dotenv import load_dotenv
import os
# First install pip install python-dotenv pip install python-dotenv
# Sec. Create a file called .env in the project folder with enviroments variables.
# Write the data in .env file, for example: USUARIO=admin
load_dotenv()
print("Environment Variable (USUARIO):", os.getenv("USUARIO"))

# ------------------------13- Python Modules and Imports--------------------------------------
print(" " * _spaces_ + "13- Python Modules and Imports")

from math import sqrt, pi

print("Square root of 16:", sqrt(16))
print("Value of Pi:", pi)

# ------------------------14- F-strings--------------------------------------
print(" " * _spaces_ + "14- F-strings")

name = "Alice"
age = 30
greeting = f"My name is {name} and I am {age} years old."
print(greeting)

# ------------------------15- Data Structures (Dicts, Sets, Tuples)--------------------------------------
print(" " * _spaces_ + "15- Data Structures (Dicts, Sets, Tuples)")

# Dictionaries
inventory = {"apple": 10, "banana": 5, "orange": 7}
inventory["grape"] = 12
print("Dictionary:", inventory)

# Sets
unique_numbers = {1, 2, 3, 3, 4, 5}
print("Set:", unique_numbers)

# Tuples
coordinates = (10.5, 20.3)
print("Tuple:", coordinates)

# ------------------------16- Enumerators--------------------------------------
print(" " * _spaces_ + "16- Enumerators")

vendedores = ["Marcus", "Amanda", "Ale", "Carol"]
vendas = [15, 29, 10, 30]
for i, vendedor23 in enumerate(vendedores):
    print(vendedor23)
    print(i)
    #print(vendas[i])

for vendedor, venda in zip(vendedores, vendas):
    print(vendedor)
    print(venda)

# ------------------------17-For-Loop--------------------------------------
print(" " * _spaces_ + "17- For-Loop")
lista_produtos = ["iphone", "ipad", "notebook"]

for item in lista_produtos:
    print(item)
    lista_precos = [1566, 2633, 5633]

for i in range(12):
    print(i)
    #i = 5

# ------------------------18-Switch/Case--------------------------------------
print(" " * _spaces_ + "18-Switch/Case")
dia = 2

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("QUinta")
elif dia == 6:
    print("sexta")
elif dia == 7:
    print("sabado")
else:
    print("Dia ivalido")

match dia :
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("QUinta")
    case 6:
        print("sexta")
    case 7:
        print("sabado")
    case outro_valor:
        print("Dia ivalido")

end_ = time.time()
print(f"Total time: {end_ - start:.4f} seconds")
