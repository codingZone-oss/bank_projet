from conextion_mysql import cursor
from validation import __valid_user_name__, __valid_password__
from funcionalitys import __Error_Handle__ as __error_handle__, palete, colors, __cleanup__, __chek__
from admin import __menu_admin__
from grh import __menu_grh__
from normal_worker import __menu_worker__


try:
    cursor.execute("select user_name, pass_word from user")
except:
    print('Some worng')

global vet
vet = list()
for line in cursor:
    vet.append(line)

def __login__(value, funtion) -> None:
    while True:
        __cleanup__()
        tester = tester1 = 0
        print(f'Log as {funtion}:')
        palete()
        user_name = __valid_user_name__('User Name: ')
        password = __valid_password__('PassWord: ')
        for v in vet:
            if user_name == v[0] and password == v[1]:
                if value == 1:
                    tester1 = 1
                    if __chek__(user_name, 'adm') == True:
                        tester = __menu_admin__(user_name)
                    else:
                        __error_handle__(value=2, text='Access Denied!')
                    
                elif value == 2:
                    tester1 = 1
                    if __chek__(user_name, 'grh') == True:
                        tester = __menu_grh__(user_name)
                    else:
                        __error_handle__(value=2, text='Access Denied!')

                    
                elif value == 3:
                    tester1 = 1
                    if __chek__(user_name, 'normal worker') == True:
                        tester = __menu_worker__(user_name)
                    else:
                        __error_handle__(value=2, text='Access Denied!')
                    
        if tester1 == 0:
            __error_handle__(value=2, text='User_name or Password Incorect!')

        if tester == 1:
            continue

        if tester == 2:
            palete()
            __cleanup__()
            __cleanup__()
            palete()
            break
        
        else:
            palete()
            resp = input('\033[33mDo you Proced: \033[m').lower()
            if resp == "y":
                continue
            while resp != "y" and resp != "n":
                palete()
                resp = input(f'{colors["red"]}Write only{colors['clear']} [y/n]').lower()
            if resp == "n":
                palete()
                __cleanup__()
                palete()
                break


def __login1__(value) -> None:
        __cleanup__()
        palete()
        user_name = __valid_user_name__('User Name: ')
        password = __valid_password__('PassWord: ')
        for v in range(1):
            if user_name in vet[0] and password in vet[1]:
                if value == 1:
                    pass
                elif value == 2:
                    pass
                elif value == 3:
                    pass
            else:
                __error_handle__(2)
  