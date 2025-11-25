from conextion_mysql import cursor
from funcionalitys import palete as pal, __admin_menu__, __cleanup__ as clen, __Error_Handle__, __while__
from add_worker import Worker



def __admin_name__(user_name: str) -> str:
    cursor.execute(f'select w.name_worker from worker w inner join user u on u.cod_worker = w.cod where u.user_name = "{user_name}"')

    vet = list()
    [vet.append(c) for cur in cursor for c in cur]
    return str(''.join(vet))


def __menu_admin__(user_name: str) -> int:
    clen()
    print('Log as Admin: ')
    pal(True, f"WellCome Dr(a): {__admin_name__(user_name)}")
    while (True):
        resp = __admin_menu__()
        match resp:
            case 1:
                obj = Worker()
                __while__(obj.date_birth)
            case 2:
                pass
                # __while__(add_repartition)
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
