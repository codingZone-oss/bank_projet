from funcionalitys import colors, __especial_character__ as char, __count_space__ as space, __count_numeric__


def __valid_name__(name1) -> str:
    while True:
        name = input(name1).split()
        if len(name) < 2:
            print(f"{colors['red']}Invalid Name!{colors['clear']}") 
            continue
        elif __count_numeric__(name) == True:
            print(f"{colors['red']}Invalid Name2 {colors['clear']}")
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

        else:
            password2 = "".join(password)
            return str(password2).strip()
        

def __valid_email__(email1) -> str:
    while True:

        email3 =  input(email1)
        email = (email3).split('@')

        if email3.count('@') != 1:
            print(f"{colors['red']}Invalid email!{colors['clear']}")
            continue
        
        if space(email) == True:
            print(f"{colors['red']}Invalid email! Can´t have Space{colors['clear']}")
            continue
    
        elif not "gmail.com" in email:
                print(f"{colors['red']}Invalid email! '@gmail.com' It´s Necessary{colors['clear']}")  
                continue
        
        else:
            email2 = "@".join(email)
            return str(email2).strip()
        

def __valid_user_name__(user_name1) -> str:
    while True:
        user_name = input(user_name1).split()
        if not len(user_name) == 1: 
            print(f"{colors['red']}Invalid User_Name!{colors['clear']}")  
            continue
        else:
            user_name2 = "".join(user_name)
            return str(user_name2).strip().lower()
        

def __valid_date__(date1) -> str:
    date = input(date1).strip()
    a = date[0:4]
    b = date[5:7]
    c = date[8:10]
    while len(date) != 10 or not a.isnumeric() or not int(a) > 1950 or not b.isnumeric() or not int(b) <= 12 or not c.isnumeric() or not int(c) <= 31 or date[4] != '-' or date[7] != '-':
        date = input(f"{colors['red']}Invalid Date, Try:2000-02-01 {colors['clear']}").strip()
        a = date[0:4]
        b = date[5:7]
        c = date[8:10]
    return str(date)

