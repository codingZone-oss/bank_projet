from funcionalitys import __Error_Handle__ as eg, colors, __especial_character__ as char, __count_space__ as space, __count_numeric__, integer, palete


def __valid_name__(name1, value:False) -> str:
    while True:
        name = input(name1).split()

        if value and not name:return ""

        if len(name) < 2:eg(value=1, text = 'Invalid Name, Must be Over 2 Words!');continue

        elif __count_numeric__(name) == True:eg(value=1, text = 'Invalid Name Numeric Data Was Found');continue

        elif any(a in char() for n in name for a in n):eg(value=1, text='Invalid Name No Special Character!');continue

        return " ".join(name).title().strip()    
            

def __valid_acount_number__(number1) -> int:
    while True:
        number = integer(number1)
        if len(str(number)) > 14 or len(str(number)) < 14:
            eg(value=1, text = 'Invalid Acount Namber,Just 14 Digits')
            continue
        else:
            return int(number)


def __valid_local_name__(name1, value=False) -> str:
    while True:
        name = input(name1)
        if value and not name:return ""
        if name == "":
            eg(value=1, text='Fill The Field')
        else:
            return str(name).title().strip()


def __valid_phone_number__(number1, value=False) -> int:
    number = input(number1)
    if value and not number:return ""
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


def __valid_identity_card__(identity_card1, value=False) -> str:
    identity_card = input(identity_card1)
    if value and not identity_card:return ""
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


def __valid_user_name__(user_name1, value=False) -> str:
    while True:
        user_name = input(user_name1).split()
        if value and not user_name:return ""

        if not len(user_name) == 1:print(f"{colors['red']}Invalid User_Name!{colors['clear']}");continue
        else:user_name2 = "".join(user_name);return str(user_name2).strip().lower()


def __valid_password__(password1, value=False) -> str:
    while True:
        password = input(password1).split()
        if value and not password:return ""

        if not len(password) == 1:print(f"{colors['red']}Invalid PassWord!{colors['clear']}");continue
        else:password2 = "".join(password);return str(password2).strip()
        

def __valid_email__(email1, value) -> str:
    while True:

        email3 =  input(email1)
        if value and not email3:return ""

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
        

def __valid_date__(date1, value=False) -> str:
    date = input(date1).strip()
    if value and not date:return ""
    a = date[0:4]
    b = date[5:7]
    c = date[8:10]
    while len(date) != 10 or not a.isnumeric() or not int(a) > 1950 or not b.isnumeric() or not int(b) <= 12 or not c.isnumeric() or not int(c) <= 31 or date[4] != '-' or date[7] != '-':
        date = input(f"{colors['red']}Invalid Date, Try:2000-02-01: {colors['clear']}").strip()
        a = date[0:4]
        b = date[5:7]
        c = date[8:10]
    return str(date)


def __valid_answerd__(func) -> str:
    palete()
    resp = input(func)
    palete()
    while resp != "y" and resp != "n":
        palete()
        resp = input(f'{colors["red"]}Write only{colors['clear']} [y/n]').lower()
        palete()
    return resp.lower()