from conextion_mysql import cursor
from funcionalitys import integer

def __select_number__(account_number: int) -> str:
    print(account_number)
    cursor.execute(f'select w.name_worker from worker w inner join user u on u.cod_worker = w.cod where u.user_name = "{account_number}"')

    vet = list()
    for cur in cursor:  
        for c in cur:
            vet.append(c)
    name = ''.join(vet)
    return str(name)

def access()-> None:
    account_number = integer('account number: ')