from conextion_mysql import cursor
from funcionalitys import palete as pal, __worker_menu__, __cleanup__ as clen, __Error_Handle__, __while__
from add_worker_client import ClientData



def __worker_name__(user_name: str) -> str:
    cursor.execute(f'select w.name_worker from worker w inner join user u on u.cod_worker = w.cod where u.user_name = "{user_name}"')

    vet = list()
    for cur in cursor:  
        for c in cur:
            vet.append(c)
    name = ''.join(vet)
    return str(name)


def __menu_worker__(user_name: str) -> int:
    clen()
    print('Log as Normal Worker: ')
    pal(True, f"WellCome Dr(a): {__worker_name__(user_name)}")
    while (True):
        resp = __worker_menu__()
        match resp:
            case 1:
                obj = ClientData()
                __while__(obj.__get_data__)
            case 2:
                pass
                # __while__(print_extract_client)
            case 3:
                pass
                # __while__(search_client)
            case 4:
                pass
                # __while__(update_client)
            case 5:
                pass
                # __while__(delete_client)
            case 6:
                tester = 1
                return tester
            case 0:
                tester = 2
                return tester
            case _:
                __Error_Handle__(1)

