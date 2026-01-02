from conextion_mysql import cursor
from funcionalitys import __Error_Handle__, __cleanup__, palete, __client_menu__, colors

def __select_client_name__(acount_number: int) -> str:
    try:
        cursor.execute(f'select c.client_name from client c join acount_access a on c.cod_acount_access = a.cod where a.acount_number = "{acount_number}";')
    except:
        print('Something Wrong')

    vet = list()
    for cur in cursor:  
        for c in cur:
            vet.append(c)
    name = ''.join(vet)
    return str(name)

def access(acount_number)-> None:
    __cleanup__()
    print(f'WellCome Exmo Sir  {colors['sky_blue']}{__select_client_name__(acount_number)}:{colors['clear']}')
    palete()
    while (True):
        resp = __client_menu__()
        match resp:
            case 1:
                pass
                # __while__(deposit)
            case 2:
                pass
                # __while__(widraw)
            case 3:
                pass
                # __while__(consult)
            case 4:
                pass
                # __while__(transfer)
            case 5:
                tester = 1
                return tester
            case 0:
                tester = 2
                return tester
            case _:
                __Error_Handle__(value=1, text='Invalid Option!')
