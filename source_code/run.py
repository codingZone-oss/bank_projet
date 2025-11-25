from funcionalitys import palete as pal, __menu__, __cleanup__ as clen,  __Error_Handle__, __while__
from user import __login__
from login_client import __login_client__

def __run__() -> None:
    clen()
    pal(True, "WellCome")

    while (True):
        resp = __menu__()
        match resp:
            case 1:
                __login__(1, 'Adm')
            case 2:
                __login__(2, 'GRH')
            case 3:
                __login__(3, 'Normal Worker')
            case 4:
                __login_client__('Client')
            case 0:
                break
            case _:
                __Error_Handle__(value=1, text='Invalid Option!')
__run__()