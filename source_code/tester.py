from funcionalitys import colors, __especial_character__ as char, __count_space__ as space, __count_numeric__ as numeric

'''def __valid_name__() -> str:
    while True:
        name = input('name: ').split()

        if len(name) < 2: # verificar se o tamanho da frase e inferior a 2
            print(f"{colors['red']}Invalid Name1 {colors['clear']}") # se for, vai entrar no loop 
            continue

        elif numeric(name) == True:
            print(f"{colors['red']}Invalid Name2 {colors['clear']}")
            continue
        
        elif [print(f"{colors['red']}Invalid Name3 {colors['clear']}") for n in name for a in n if a in char()]:
            continue

        else:
            name1 = " ".join(name)
            print(str(name1))
            return str(name1).title().strip()

print(type(__valid_name__()))'''


'''def __valid_password__() -> None:
    while True:
        password = input("password: ").split()
        if not len(password) == 1: 
            print(f"{colors['red']}Invalid PassWord!{colors['clear']}")  
            continue

        elif [print(f"{colors['red']}Invalid password!{colors['clear']}") for p in password for s in p if s.isspace()]:
            continue

        else:
            print(password)
            password2 = " ".join(password)
            print(password2)
            return str(password2).strip()
        
print(type(__valid_password__()))'''


'''def __valid_email__() -> str:
    while True:
        email1 = input('email: ')
        email = (email1).split('@')
        print(email)

        if email1.count('@') != 1:
            print(f"{colors['red']}Invalid email!{colors['clear']}")
            continue

        elif space(email) == True:
            print(f"{colors['red']}Invalid email! Can´t have Space{colors['clear']}")
            continue
    
        elif not "gmail.com" in email:
                print(f"{colors['red']}Invalid email! '@gmail.com' It´s Necessary{colors['clear']}")  
                continue
        
        else:
            print(email)
            email2 = "@".join(email)
            print(email2)
            return str(email2).strip()
        
     
print(type(__valid_email__()))'''


'''def __valid_user_name__() -> str:
    while True:
        user_name = input('user_name: ').split()
        if not len(user_name) == 1: 
            print(f"{colors['red']}Invalid PassWord!{colors['clear']}")  
            continue
        else:
            print(user_name)
            user_name2 = "".join(user_name)
            print(user_name2)
            return str(user_name2).strip()

print(type(__valid_user_name__()))'''


'''def __valid_date__() -> str:
    date = input('01/02/2000: ').strip()
    a = date[0:2]
    b = date[3:5]
    c = date[6:10]

    while len(date) != 10 or not a.isnumeric() or int(a) > 31 or not b.isnumeric() or int(b) > 12 or not c.isnumeric() or int(c) < 1950 or date[2] != '/' or date[5] != '/':
        date = input(f"{colors['red']}Invalid Date, Try:01/02/2000 {colors['clear']}").strip()
        a = date[0:2]
        b = date[3:5]
        c = date[6:10]

    # phone_number = "".join(number.split())
    print(date)
    return (date)
print(type(__valid_date__()))'''

