from conextion_mysql import cursor
from validation import __valid_user_name__, __valid_password__
from funcionalitys import __Error_Handle__ as __error_handle__, palete, colors, __cleanup__
from admin import printer
from grh import printer2
from normal_worker import NormalWorker


try:
    cursor.execute("select user_name, pass_word from user")
except:
    print('Some worng')

global vet
vet = list()
for line in cursor:
    for l in line:
        vet.append(l)

def __login__(value, funtion) -> None:
    while True:
        __cleanup__()
        tester = False
        print(f'Log as {funtion}:_ ')
        palete()
        print(vet)
        user_name = __valid_user_name__('User Name: ')
        password = __valid_password__('PassWord: ')
        for v in range(1):
            if user_name in vet[0] and password in vet[1]:
                if value == 1:
                    printer()
                elif value == 2:
                    printer2()
                elif value == 3:
                    worker = NormalWorker
                    tester = worker._menu(user_name)
            else:
                __error_handle__(2)
        if tester == True:
            continue
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
                    printer()
                elif value == 2:
                    printer2()
                elif value == 3:
                    pass
            else:
                __error_handle__(2)
  