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
The __init__.py file transforms a directory into a Python package, allowing the contents of that directory to be imported
into other modules, You can use the special __all__ attribute in __init__.py to explicitly define the items that will be exposed when using
from pacote import * .
relative import
prospector
memory profiler, cProfiler, snakeviz timeit, %timeit, repeat
Common folders: src(model, view, controller), test, docs

project_name/
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
├── LICENSE
├── docs/
│   └── ...  # Documentation files
├── src/
│   ├── project_name/
│   │   ├── __init__.py
│   │   ├── module1.py
│   │   ├── module2.py
│   │   ├── subpackage/
│   │   │   ├── __init__.py
│   │   │   ├── submodule1.py
│   │   │   └── submodule2.py
│   └── tests/
│       ├── __init__.py
│       ├── test_module1.py
│       ├── test_module2.py
│       └── subpackage/
│           ├── __init__.py
│           ├── test_submodule1.py
│           └── test_submodule2.py
└── scripts/
    ├── script1.py
    └── script2.py

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


# ------------------------19-Dataclasses--------------------------------------
print(" " * _spaces_ + "19-Dataclasses") #To create classes to storage data.

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    ativo: bool = True  # Atributo com valor padrão

# Criando instâncias
p1 = Pessoa(nome="Alice", idade=30)
p2 = Pessoa(nome="Bob", idade=25, ativo=False)

print(p1)  # Output: Pessoa(nome='Alice', idade=30, ativo=True)
print(p2)  # Output: Pessoa(nome='Bob', idade=25, ativo=False)

# Comparação
print(p1 == p2)  # Output: False



# ------------------------20-Include modules from directories--------------------------------------
print(" " * _spaces_ + "20-Include modules from directories") 

#These lines are used to configure the execution environment to
#include modules from parent or ancestor directories in the project.
#This is especially useful in large projects with multiple folders.

#Consider the following project structure:
project/
├── main.py
├── module/
│   └── utils.py

#If you want to import utils.py into main.py but module/ is not in sys.path, the lines above allow you to include module/ in the module search path:

# main.py
import sys  
# Imports the `sys` module, which provides access to system-specific parameters and functions, including `sys.path`.
from pathlib import Path  
# Imports the `Path` class from the `pathlib` module. `Path` is used for object-oriented file and directory manipulation.
file = Path(__file__).resolve()  
# Creates a `Path` object representing the current file (`__file__`) and resolves it to its absolute path.  
# `__file__` is a special variable that holds the path to the script being executed.  
# `resolve()` ensures that the path is absolute and resolves any symbolic links.
parent, root = file.parent, file.parents[1]  
# `file.parent` retrieves the directory containing the current file.  
# `file.parents[1]` navigates up one level in the directory tree (to the grandparent directory).  
# Assigns these two directories to the variables `parent` and `root`.
sys.path.append(str(root))  
# Converts `root` (the grandparent directory) to a string and appends it to `sys.path`.  
# `sys.path` is a list of directories that Python searches for modules when importing.  
# Adding `root` ensures that Python can locate modules in the grandparent directory.
from module.utils import my_function  
# Imports the `my_function` function from the `utils` module, which is located in the `module` directory.  
# This import works because `root` (which includes the `module` directory) has been added to `sys.path`.

#This way, you can use my_function normally.


# ------------------------21-Regular expressions--------------------------------------
print(" " * _spaces_ + "21-Regular expressions") 


#Regular expressions in Python are a powerful tool for finding, analyzing, and manipulating text based on specific patterns.
#They are accessed through the re module in the standard library.

Main Functions in the re Module
1->re.match()
#Checks if the pattern matches the beginning of the string.

text = "Hello, world!"
result = re.match(r"Hello", text)
print(result)  # Output: <re.Match object>

2->re.search()
#Searches for the pattern anywhere in the string.

text = "Welcome to the Python world!"
result = re.search(r"world", text)
print(result.group())  # Output: "world"

3->re.findall()
#Returns all occurrences of the pattern in a list.

text = "The number 42 appears here 42 times."
result = re.findall(r"\d+", text)  # Looks for digits
print(result)  # Output: ['42', '42']

4->re.finditer()
#Similar to findall, but returns an iterator of Match objects.

text = "abc123xyz456"
for match in re.finditer(r"\d+", text):
    print(match.group())  # Output: 123 and 456
5->re.sub()
#Replaces all occurrences of the pattern with a new string.

text = "Hello, world!"
new_text = re.sub(r"world", "Python", text)
print(new_text)  # Output: "Hello, Python!"

#Key Metacharacters
.: Any character (except newline).
^: Start of the string.
$: End of the string.
*: Zero or more occurrences.
+: One or more occurrences.
?: Zero or one occurrence.
[]: Character class.
E.g., [a-z] (any lowercase letter from a to z).
|: OR.
E.g., a|b (matches a or b).
\d: A digit (equivalent to [0-9]).
\w: An alphanumeric character or underscore.
\s: A whitespace character.

#--------------------------------------Examples of Usage------------------------
#1->Validating an Email
email = "example@domain.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
result = re.match(pattern, email)
print(bool(result))  # Output: True

#2->Extracting Numbers from Text
text = "Temperatures were 20°C yesterday and 25°C today."
numbers = re.findall(r"\d+", text)
print(numbers)  # Output: ['20', '25']

#3->Replacing Words
text = "Python is amazing!"
new_text = re.sub(r"amazing", "fantastic", text)
print(new_text)  # Output: "Python is fantastic!"

#4->Splitting Words in a Sentence
sentence = "Python is amazing and powerful."
words = re.split(r"\s", sentence)  # Splits by spaces
print(words)  # Output: ['Python', 'is', 'amazing', 'and', 'powerful.']

#---------Common Flags in Regular Expressions-------
re.IGNORECASE (re.I): Ignores case sensitivity.
re.MULTILINE (re.M): Allows ^ and $ to match the start and end of each line.
re.DOTALL (re.S): Makes . match newlines.

#Example with a flag:
text = "Python is Powerful.\nAnd amazing!"
result = re.findall(r"^And", text, flags=re.MULTILINE)
print(result)  # Output: ['And']

#---------Tips for Working with Regular Expressions--------
Use online tools to test patterns, such as regex101.com.
Keep patterns clear and well-commented to improve readability.
Break down more complex patterns into smaller parts for incremental validation.



# ---------------------------------------------21-yield--------------------------------------------------------
print(" " * _spaces_ + "21-yield") 
    
#The yield keyword in Python is used in a generator function to produce a value and pause the function's execution,
#preserving its state for resumption. This allows efficient handling of sequences or data streams without storing all the data in memory at once.

#When a function contains yield, it becomes a generator function. Instead of returning a single value and exiting,
#the function can produce a series of values, one at a time, as the generator object is iterated.

#Key Advantages of yield
#Memory Efficiency: It generates values on the fly, which is ideal for working with large datasets or infinite sequences
#State Retention: The generator function retains its state between calls, avoiding repeated computations.
"""                                                   
Key Differences Between yield and return
Aspect        	    yield        	                        return
Behavior	        Pauses the function and resumes later.	Exits the function.
Function Type	    Turns the function into a generator.	Regular function.
Usage in Iteration	Produces a sequence of values lazily.	Produces a single value.
"""
#this code below print each yield value.
def simple_generator():
    yield 4
    yield 7
    yield 9
gen = simple_generator()
print(next(gen))  # Output: 4
print(next(gen))  # Output: 7
print(next(gen))  # Output: 9

#this code below print each line of the vendas.csv file.
def ler_csvlnome_arquivdjz
    yield from open(nome_arquivo, "r")
vendas = ler_csv("vendas.csv")
for venda in vendas:
    print(venda)

# ---------------------------------------------22-Dependency injection--------------------------------------------------------
print(" " * _spaces_ + "22-Dependency injection") 

#Dependency injection is a design technique that allows objects to receive their dependencies from external sources rather than
#creating them internally. This promotes more modular, flexible, and testable code.
#In Python, dependency injection can be implemented in several ways, including:
#Constructor Injection: Dependencies are passed as parameters when the object is created.

python
Copiar código
class Repository:
    def get_data(self):
        pass

class Service:
    def __init__(self, repository: Repository):
        self.repository = repository

    def process_data(self):
        data = self.repository.get_data()
        # Process the data
#Method Injection: Dependencies are provided through specific methods.

python
Copiar código
class Service:
    def __init__(self):
        self.repository = None

    def set_repository(self, repository: Repository):
        self.repository = repository

    def process_data(self):
        if not self.repository:
            raise ValueError("Repository not set.")
        data = self.repository.get_data()
        # Process the data
#Property Injection: Dependencies are assigned directly to object properties.

python
Copiar código
class Service:
    def __init__(self):
        self._repository = None

    @property
    def repository(self):
        if not self._repository:
            raise ValueError("Repository not set.")
        return self._repository

    @repository.setter
    def repository(self, repository: Repository):
        self._repository = repository

    def process_data(self):
        data = self.repository.get_data()
        # Process the data

                                                   


end_ = time.time()
print(f"Total time: {end_ - start:.4f} seconds")
