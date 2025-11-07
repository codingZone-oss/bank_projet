from conextion_mysql import cursor
from funcionalitys import palete as pal, __worker_menu__, __cleanup__ as clen, __Error_Handle__

class MySql:

    def __init__(self):
        pass
     
    def _innerjoin(self, worker_name) -> None:
        cursor.execute(f'select w.name_worker from worker as w inner join user as u where u.cod_worker = w.cod and user_name = {worker_name}')
        vet = list()
        for cur in cursor:
            for c in cur:
                vet.append(c)
        name = ''.join(vet)
        return name


class NormalWorker(MySql):

    def __init__(self):
        super().__init__()

    def _menu(user_name) -> bool:
        clen()
        print('Log as Normal Worker: ')
        worker_name = self._innerjoin(user_name)
        pal(True, f"WellCome Dr(a): {worker_name}")
        while (True):
            resp = __worker_menu__()
            match resp:
                case 1:
                    pass
                    # __while__(add_client)
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
                case 0:
                    tester = True
                    return tester
                case _:
                    __Error_Handle__(1)
obj = MySql()
print(obj._innerjoin())