from conextion_mysql import cursor

class InsertClient:

    def __select__(self) -> list:
        cursor.execute('select cod, cod_repartition, cod_acount_access from client')

        vet = list()
        for curs in cursor:
            vet.append(curs)
        print(vet)

    def __init__(self) -> None:
        self.__cod = 0
        self.__name = None
        self.__city = None
        self.__avenue = None
        self.__street = None
        self.__district = None
        self.__phone_number = None 
        self.__neighborhood = None
        self.__identity_tiket = None
        self.__cod_repartition = 0
        self.__cod_acount_access = 0

    def __insert_data__(self) -> None:
        cursor.execute(f"insert into client values({self.__cod}, '{self.__name}', '{self.__identity_tiket}','{self.__phone_number}', '{self.__city}', '{self.__district}', '{self.__avenue}', '{self.__neighborhood}', '{self.__street}', {self.__cod_repartition}, {self.__cod_acount_access});")

    def print1(self) :
        return self.__cod
    
obj = InsertClient()
obj.__select__()