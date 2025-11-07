import os


colors = {"clear":  "\033[m",
         "red":     "\033[31m",
         "green":   "\033[32m",
         "yelow":   "\033[33m",
         "blue":    "\033[34m",
         "purple":  "\033[35m",
         "sky_blue": "\033[36m",
         "gray":    "\033[37m"}


def __Error_Handle__(value=0, staff=None) -> None:
    if value == 1:
        palete()
        print(f'{colors["red"]}Invalid Option!{colors["clear"]}'.center(40))
        palete()
    elif value == 2:
        palete()
        print(f'{colors["red"]}user_name or password Incorect!{colors["clear"]}'.center(40))
    else:
        palete()
        print(f'{colors["red"]}Write only {staff} values!{colors["clear"]}'.center(40))
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


def __menu__() -> int:
    print("1. Log as Adm")
    print("2. Log as Grh")
    print("3. Log as normal worker")
    print("4. Log as client")
    print("0. Leav..")
    palete()
    resp = integer(f"{colors['yelow']}what´s your choice: {colors['clear']}")
    return resp


def __worker_menu__() -> int:
    print("1. Add Client")
    print('2  Print Client Extract')
    print("3. Search Client")
    print("4. Update Client")
    print("5. Delete Client")
    print("0. Leav..")
    palete()
    resp = integer(f"{colors['yelow']}what´s your choice: {colors['clear']}")
    return resp


def integer(value):
    while True:
        try:
            num = int(input(value))
        except ValueError:
            __Error_Handle__(staff='Integer')
            continue
        else:
            return num


def __especial_character__() -> list:
    list = ["!", "@", "#", "$", "%", "&", "/", "*", "(", ")", "=", "'", '"', "-", "_", ">", "<", ";", ".", ":", ",", "´", "+", "~", "|", "\\", "}", "{", "]", "[", "€", "§", "£", ""]
    
    return list


def __count_space__(values=False) -> bool:
     for v in values:
        for a in v:
             if a.isspace():
                return True


def __count_numeric__(values=False) -> bool:
     for v in values:
        for a in v:
             if a.isnumeric():
                return True


def real(test) -> float:
    while True:
        try:
            num = float(input(test))
        except ValueError:
            __Error_Handle__(staff='Real')
            continue
        else:
            return num


def __while__(argument) -> None:
    while True:
        argument
        palete()
        resp = input('\033[33mDo you Proced: \033[m').lower()
        if resp == "y":
            continue
        while resp != "y" and resp != "n":
            palete()
            resp = input(f'{colors["red"]}Write only{colors['clear']} [y/n]').lower()
        if resp == "n":
            palete()
            break


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


'''