from funcionalitys import __cleanup__, integer, palete, __while__, __Error_Handle__, colors
from conextion_mysql import cursor
from acount_access import access
from validation import __valid_acount_number__

def __select_number__() -> list:
    try:
        cursor.execute(f'select acount_number from acount_access')
    except:
        print("Something wrong")

    vet = list()
    [vet.append(c) for cur in cursor for c in cur]
    return list(vet)


def __login_client__(client) -> None:
    while True:
        __cleanup__()
        print(f'Log as {client}:')
        palete()
        account_number = __valid_acount_number__('account number: ')
        tester = tester1 = 0
        for s in __select_number__():
            if account_number == s:
                tester1 = access(account_number)
                tester = 1

        if tester == 0:
            __Error_Handle__(value=2, text='Acount Number Not found!')

        if tester1 == 1:
            continue

        if tester1 == 2:
            palete()
            __cleanup__()
            palete()
            break

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