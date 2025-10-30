from funcionalitys import colors, __character__ as char


def __valid_name__(name1) -> str:
    while True:
        name = input(name1).split()
        if len(name) < 2: # verificar se o tamanho da frase e inferior a 2
            print(f"{colors['red']}Invalid Name!{colors['clear']}") # se for, vai entrar no loop 
            continue
        elif [print(f"{colors['red']}Invalid Name!{colors['clear']}") for n in name for a in n if len(n) < 2 or a.isnumeric()]:
            continue
        elif [print(f"{colors['red']}Invalid Name!{colors['clear']}") for n in name for a in n if a in char()]:
            continue
        else:
            name1 = " ".join(name)
            return str(name1).title().strip()


def __valid_phone_number__(number1) -> int:
    number = input(number1)
    a = number[0:3]
    b = number[4:7]
    c = number[8:10]
    while len(number) != 11 or not a.isnumeric or not b.isnumeric() or not c.isnumeric() or not number[0] == '9' or not number[3].isspace() or not number[7].isspace():
        number = input(f"{colors['red']}Invalid Phone Number: {colors['clear']}")
        a = number[0:3]
        b = number[4:7]
        c = number[8:10]

    phone_number = "".join(number.split())
    return int(phone_number)


def __valid_identity_card__(identity_card1) -> str:
    identity_card = input(identity_card1)
    a = identity_card[0:9]
    b = identity_card[9:11]
    c = identity_card[11:14]
    while len(identity_card) != 14 or not a.isnumeric() or not b.isalpha() or not c.isnumeric():
        identity_card = input(f"{colors['red']}Invalid Identity Card: {colors['clear']}")
        a = identity_card[0:9]
        b = identity_card[9:11]
        c = identity_card[11:14]
    return identity_card


def __valid_gender__(gender1) -> str:
    gender = input(gender1)
    while gender != 'm' and gender != 'f' :
        gender = input(f'{colors['red']}Write only [M/F]{colors['clear']}')
    return  gender.upper().strip()


def __valid_password__(password1) -> str:
    while True:
        password = input(password1).split()
        if not len(password) == 1: 
            print(f"{colors['red']}Invalid PassWord!{colors['clear']}")  
            continue

        elif [print(f"{colors['red']}Invalid password!{colors['clear']}") for p in password for s in p if s.isspace()]:
            continue

        else:
            password2 = "".join(password)
            return str(password2).strip()
        
