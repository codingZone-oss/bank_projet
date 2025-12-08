from conextion_mysql import cursor
from funcionalitys import palete as pal, __grh_menu__, __cleanup__ as clen, __Error_Handle__



def __grh_name__(user_name: str) -> str:
    cursor.execute(f'select w.name_worker from worker w inner join user u on u.cod_worker = w.cod where u.user_name = "{user_name}"')

    vet = list()
    [vet.append(c) for cur in cursor for c in cur]
    return str(''.join(vet))


def __menu_grh__(user_name: str) -> int:
    while (True):
        clen()
        print('Log as GRH Worker: ')
        pal(True, f"WellCome Dr(a): {__grh_name__(user_name)}")
        resp = __grh_menu__()
        match resp:
            case 1:
                pass
                # __while__(search_client)
            case 2:
                pass
                # __while__(update_client)
            case 3:
                pass
                # __while__(delete_client)
            case 4:
                tester = 1
                return tester
            case 0:
                tester = 2
                return tester
            case _:
                __Error_Handle__(1)