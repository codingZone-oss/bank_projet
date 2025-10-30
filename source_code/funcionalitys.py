import os

colors = {"clear":  "\033[m",
         "red":     "\033[31m",
         "green":   "\033[32m",
         "yelow":   "\033[33m",
         "blue":    "\033[34m",
         "purple":  "\033[35m",
         "sky_blue": "\033[36m",
         "gray":    "\033[37m"}

def __Error_Handle__(value=False) -> None:
    if value == True:
        palete()
        print(f'{colors["red"]}Invalid Option!{colors["clear"]}'.center(40))
        palete()
    else:
        palete()
        print(f'{colors["red"]}Write only int values!{colors["clear"]}'.center(40))
        palete()

def __cleanup__():
    os.system('cls')

def palete(boolean=False, text=None):
    if boolean == True:
        print("-" * 30)
        print(text. center(30))
        print("-" * 30)
    else:
        print("_" * 30)


def menu() -> int:
    print("1. Log as Adm")
    print("2. Log as Grh")
    print("3. Log as normal worker")
    print("4. Log as client")
    print("0. Leav..")
    palete()
    resp = integer(f"{colors['yelow']}what´s your choice: {colors['clear']}")
    return resp


def integer(value):
    while True:
        try:
            num = int(input(value))
        except ValueError:
            __Error_Handle__()
            continue
        else:
            return num
        
def __character__() -> list:
    list = ["!", "@", "#", "$", "%", "&", "/", "*", "(", ")", "=", "'", '"', "-", "_", ">", "<", ";", ".", ":", ",", "´", "+", "~", "|", "\\", "}", "{", "]", "[", "€", "§", "£", ""]
    
    return list
'''
def bilhete(bi1) -> str:
    bi = input(bi1)
    a = bi[0:9]
    b = bi[9:11]
    c = bi[11:14]
    while len(bi) != 14 or not a.isnumeric() or not b.isalpha() or not c.isnumeric():
        bi = input('\033[1;31mNúmero do Bilhete Inválido: \033[m')
        a = bi[0:9]
        b = bi[9:11]
        c = bi[11:14]
    return bi

def iguais(num) -> list:
    numero1 = ()
    numero2 = []
    numero = input(num).split()

    if len(numero) > 1:
        for d in range(1):
            numero1 = numero

    for c in numero1:
        numero2.append(int(c))
    return numero2

def real(teste) -> float:
    while True:
        try:
            num = float(input(teste))
        except ValueError:
            print(f'\033[31mEscreva apenans valores numericos! \033[m')
            continue
        else:
            return num

def genero(teste) -> str:
    coisa = input(teste)
    while coisa != 'm' and coisa != 'f' :
        coisa = input('escreva apenas [M/F]')
    return  coisa

def return_int() -> int:
    conta = [0, 1, 2, 3, 4, 5, 6, 7]
    shuffle(conta)
    numero_unico = int("".join(map(str, conta)))
    return numero_unico


def enquanto(argumento):
    while True:
        argumento()
        resp = input('\033[33mQuer continuar: \033[m').lower()
        if resp == "s":
            continue
        while resp != "s" and resp != "n":
            design()
            resp = input('\033[31mDigite Apenas\033[m [s/n]').lower()
        if resp == "n":
            break'''