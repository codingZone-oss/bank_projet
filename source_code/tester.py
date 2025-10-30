from funcionalitys import colors, __character__ as char

'''def __valid_name__() -> str:
    while True:
        name = input('name: ').split()

        if len(name) < 2: # verificar se o tamanho da frase e inferior a 2
            print(f"{colors['red']}Invalid Name: {colors['clear']}") # se for, vai entrar no loop 
            continue

        elif [print(f"{colors['red']}Invalid Name: {colors['clear']}") for n in name for a in n if len(n) < 2 or a.isnumeric()]:
            continue
        
        elif [print(f"{colors['red']}Invalid Name: {colors['clear']}") for n in name for a in n if a in char()]:
            continue

        else:
            name1 = " ".join(name)
            print(str(name1))
            return str(name1).title().strip()

print(type(__valid_name__()))'''

# def __valid_password__() -> str:
#     password = input('password: ').split()
#     print(password)
#     while len(password) > 1:
#         password = input(f'{colors['red']} Invalid PassWord{colors['clear']}').split()
#     return str(password)

# __valid_password__()

'''    name = 'es tanislau do santos'.split() # receber a frase, e separa-la 

    while len(name) < 2: # verificar se o tamanho da frase e inferior a 2
        name = input(f"{colors['red']}Invalid Name: {colors['clear']}").split() # se for, vai entrar no loop

    print(name) # se não for, printar a a frase separada

    for n in name: # dividir a frase em palavras

        for a  in n: # dividir as palavras em letras

            # a primeira consição verifica se o tamnho das palavras é igual ou inferior a 2

            # a segunda verifica se existe no meu de todas as letras um digito numérico

            # se uma das condições acima não for verdadeira a varialvel nome recebe uma outra frase, e se faz a ultima condição que é: 
            # se o tamanho da frase for nferior a 2 de novo 

            while len(n) <= 2 or a.isnumeric() or len(name) < 2:
                name = input(f"{colors['red']}Invalid Name: {colors['clear']}").split()
                for n in name:
                    pass

    name1 = " ".join(name)
    return str(name1).title().strip()'''

def __valid_password__() -> None:
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
        
print(type(__valid_password__()))