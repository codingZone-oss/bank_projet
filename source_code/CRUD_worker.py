from conextion_mysql import cursor
from funcionalitys import colors as c1, __cleanup__, integer, menu_worker, palete as pl, __Error_Handle__
from validation import __valid_local_name__, __valid_acount_number__, __valid_identity_card__, __valid_phone_number__
from news_data import NewsData

class SearchWorker:

    def select(self, column, value) -> list:
        cursor.execute(f"select name_worker from worker where {column} like '%{value}%';")

        vet = list()
        [vet.append(v) for ve in cursor for v in ve] 
        return vet

    def __search__(self) -> None:
        __cleanup__()
        resp = menu_worker()
        tester = False
        match resp:
            case 1:
                name = __valid_local_name__('Enter the Name: ');pl()
                for c in self.select('name_worker', name):print(f"{c1['purple']}{c}{c1['clear']}")
                if len(self.select('name_worker', name)) == 0: tester = True
                else:return self.select('name_worker', name)

            case 2:
                phone_number = __valid_phone_number__('Enter the Phone Number: ');pl()
                for c in self.select('phone_number', phone_number):print(f"{c1['purple']}{c}{c1['clear']}")
                if len(self.select('phone_number', phone_number)) == 0: tester = True
                else:return self.select('phone_number', phone_number)

            case 3:
                identity_card = __valid_identity_card__('Enter the Identity Card Number: ');pl()
                for c in self.select('number_identity_card', identity_card):print(f"{c1['purple']}{c}{c1['clear']}")
                if len(self.select('number_identity_card', identity_card)) == 0: tester = True
                else:return self.select('number_identity_card', identity_card)

            case 0:pass
            case _:__Error_Handle__(value=1, text='Invalid Option!')

        if tester == True:__Error_Handle__(value=1, text='Name Not Found!');return True

class UpdateWorker(SearchWorker):

    def __update__(self) -> None:
        value = list()
        tester = self.__search__()
        if tester == True:pass
        else:
            if len(tester) == 1:obj = NewsData(tester[0]); obj.all_function()
            else:
                for v in range(len(tester)):value.append(v)
                while True:
                    resp = integer(f"Select the Worker to Update {value}: ")
                    if resp in value: obj = NewsData(tester[resp]); obj.all_function();break
                    else:__Error_Handle__(value=1, text='Invalid Option!');continue

class UpdateDelete(SearchWorker):
    pass
# obj1 = UpdateWorker()
# obj1.__update__()