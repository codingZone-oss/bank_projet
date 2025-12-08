from funcionalitys import menu_client, __Error_Handle__, __cleanup__, colors, palete as pl
from conextion_mysql import cursor
from validation import __valid_local_name__, __valid_identity_card__, __valid_acount_number__


class SearchClient:

    def select(self, column, value) -> list:
        cursor.execute(f"select c.client_name from client c join acount_access a on c.cod_acount_access = a.cod where {column} like '%{value}%'")

        vet = list()
        [vet.append(v) for ve in cursor for v in ve] 
        return vet

    def __search__(self) -> None:
        __cleanup__()
        resp = menu_client()
        tester = False
        match resp:
            case 1:
                name = __valid_local_name__('Enter the Name: ');pl()
                for c in self.select('client_name', name):print(f"{colors['purple']}{c}{colors['clear']}")
                if len(self.select('client_name', name)) == 0: tester = True

            case 2:
                acount_number = __valid_acount_number__('Enter the Acount Number: ');pl()
                for c in self.select('acount_number', acount_number):print(f"{colors['purple']}{c}{colors['clear']}")
                if len(self.select('acount_number', acount_number)) == 0: tester = True

            case 3:
                identity_card = __valid_identity_card__('Enter the Identity Card Number: ');pl()
                for c in self.select('number_identity_card', identity_card):print(f"{colors['purple']}{c}{colors['clear']}")
                if len(self.select('number_identity_card', identity_card)) == 0: tester = True
            case 0:
                pass
            case _:
                __Error_Handle__(value=1, text='Invalid Option!')

        if tester == True:
            __Error_Handle__(value=1, text='Name Not Found!')

        return None


class UpdateClient(SearchClient):
    
    def __update__(self) -> None:
        self.__search__()
        pass


class DeletClient(SearchClient):
    pass


# obj = SearchClient()
# obj.__search__()
