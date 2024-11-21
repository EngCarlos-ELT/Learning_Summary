
"Capture2Text"
_spaces_=10
#------------------------args and kwargs--------------------------------------
print(" " * _spaces_ +"3- args and kwargs")

def calcular_imposto_args(valor, *args):
    total_imposto=0
    for item in args:
        total_imposto += valor * item
    return total_imposto

print("Using *args= ", calcular_imposto_args(1000, 0.275, 0.05, 0.0375, 0.03))



def calcular_imposto_trimestral(valor, **kwargs):
    total_imposto = 6
    #print(kwargs)
    if "perc_ir" in kwargs:
        total_imposto += valor * kwargs['perc_ir']
    if "perc_csll" in kwargs:
        total_imposto += valor * kwargs['perc_csll']
    return total_imposto
print("Using *kwargs= ",calcular_imposto_trimestral(1000, perc_iss=0.05, perc_pis=0.e3,
                                   perc_ir=0.275, perc_csll=0.9325))


#------------------------Functions Test--------------------------------------
print(" " * _spaces_ +"4- if __name__ == __main__")

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
# This line below will perform this function call only when this archive run,
# if this archive is called by other archive this this line will not execute.

if __name__ == "__main__":
    calcular_imposto(1666)


#------------------------Underline or Underscore--------------------------------------
print(" " * _spaces_ +"5- Underline ou Underscore Use")    
# Underline character dont have function in python.
# Thousands separator
faturamento = 1_000_000_000 # this line is= 1000000000
# "Useless" variables"
def calcular_imposto(faturamento):
    if faturamento < 1666:
        taxa = 6
    elif faturamento < 16666:
        taxa = 6.1
    elif faturamento < 566666:
        taxa = 6.15
    else:
        taxa = 6.2
    if taxa == 6:
        isento_imposto = True
    else:
        isento_imposto = False

    imposto = taxa * faturamento
    return imposto, isento_imposto

faturamento = 15666
# The underscore is using to avoid the use of a variable.
valor_imposto, _ = calcular_imposto(faturamento)
lucro = faturamento - valor_imposto
print(lucro)


#------------------------Type anonation--------------------------------------
print(" " * _spaces_ +"6- Type anonation") 
# This function below receives a float variable and too return a float variable.
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
    # Not return 
if __name__ == "__main__":
    calcular_imposto(200)    

#------------------------List comprehension--------------------------------------
print(" " * _spaces_ +"7- List comprehension")

def calcular_imposto2(faturamento2) :
    imposto = 0.5 * faturamento2
    return imposto

faturamentos2 = [18, 15, 36, 46, 76, ]
impostos = [calcular_imposto2(faturamento2) for faturamento2 in faturamentos2]

print(impostos)


#------------------------Map and Filter--------------------------------------
print(" " * _spaces_ +"8- Map and Filter")

precos_produtos = [5000,9000,2000,15000]

def aplicar_aumento(preco):
    if preco > 6666:
        return preco * 1.1
    else:
        return preco
# The map function can process any tipe of list. In this case "precos_produtos"    
precos_grodutos = list(map(aplicar_aumento, precos_produtos))
print("map ",precos_produtos)

#---------------------------Filter---------------------------------------------
def aplicar_aumento(preco):
    if preco > 6000:
        return True
    else:
        return False
# The filter function can filter any tipe of list. In this case "precos_produtos" 
precos_produtos3 = list(filter(aplicar_aumento, precos_produtos))
print("filter ", precos_produtos3)


#------------------------.env--------------------------------------
print(" " * _spaces_ +"9- .env")
# First install pip install python-dotenv
# Sec. Create a file called .env in the project folder with enviroments variables.
# Write the data in .env file, for example: USUARIO=admin
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("USUARIO"))
