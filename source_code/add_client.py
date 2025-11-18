from conextion_mysql import cursor
from validation import __valid_name__, __valid_identity_card__, __valid_phone_number__, __valid_email__, __valid_gender__, __valid_date__
from funcionalitys import palete, __Error_Handle__, acount_number, colors, __cleanup__, palete2
from datetime import date

class CheckData:

    def __check_age__(self, date_birth) -> bool:

        var = int(date_birth[0:4])
        age = date.today().year - var
        if age >= 18:
            return True
        else:
            return False
        
        
    def __check_email__(self, email) -> bool:
        try:
            cursor.execute('select email from client')
        except:
            print('something wrong')

        vet = list()
        for line in cursor:
            for cur in line:
                vet.append(cur)
        tester = 0
        for v in vet:
            if email == v:
                tester = 1

        if tester == 1:
            return True
        else:
            return False


    def __check_phone_number__(self, phone_number) -> bool:
          
        try:
            cursor.execute('select phone_number from client')
        except:
            print('something wrong')

        vet = list()
        for line in cursor:
            for cur in line:
                vet.append(cur)
        tester = 0
        for v in vet:
            if phone_number == v:
                tester = 1

        if tester == 1:
            return True
        else:
            return False


    def __check_identity_card__(self, identity_card) -> bool:

        try:
            cursor.execute('select number_identity_card from client')
        except:
            print('something wrong')

        vet = list()
        for line in cursor:
            for cur in line:
                vet.append(cur)
        tester = 0
        for v in vet:
            if identity_card == v:
                tester = 1

        if tester == 1:
            return True
        else:
            return False


class ClientData(CheckData):

    def __init__(self, user_name, worker_name):
        super().__init__()
        self.__user_name = user_name
        self.__worker_name = worker_name

    def __get_data__(self) -> None:
        __cleanup__()
        print(f'WORKER: {colors['purple']}{self.__worker_name} {colors['clear']}')

        palete2(f'{colors['sky_blue']}Creating Client Acount {colors['clear']}')
        
        palete(True, f'{colors['yelow']}Personal Data{colors['clear']}')

        name = __valid_name__('Enter The Name: ')
        identity_card = __valid_identity_card__('Enter The Identity Card Number: ')
        phone_number = __valid_phone_number__('Enter The Phone Number: ')
        email = __valid_email__('Enter The Email: ')
        gender = __valid_gender__('Enter The Gender: ')
        date_birth = __valid_date__('Enter The Date Birth: ')

        palete(True, 'Address Data')

        nationality = input('Enter The Nationality: ')
        city = input('Enter The City: ')
        avenue = input('Enter The Avenue: ')
        street = input('Enter The Street: ')
        district = input('Enter The District: ')
        neighborhood = input('Enter The Neighborhood: ')


        if self.__check_age__(date_birth) == False:
            __Error_Handle__(5)

        elif self.__check_email__(email) == True:
            __Error_Handle__(6)

        elif self.__check_phone_number__(phone_number) == True:
            __Error_Handle__(7)

        elif self.__check_identity_card__(identity_card) == True:
            __Error_Handle__(8)
            
        else:
            try:
                obj = InsertClient(name, phone_number, email, gender, date_birth, identity_card, nationality, city, avenue, street, district, neighborhood)

                obj.__insert_transfer__()
                obj.__inert_deposit__()
                obj.__insert_widraw__()
                obj.__insert_acount_data__(acount_number())
                obj.__insert_client_data__(self.__user_name)
                
                palete(True, f'{colors["sky_blue"]}{name} Acount Created with Success!{colors["clear"]}')
                print(acount_number())
                
            except Exception as e:
                print('There is a Mistake to Insert:', e)
            finally:
                cursor.close()


class InsertClient:

    def __init__(self, name, phone_number, email, gender, date_birth, identity_card, nationality, city, avenue, street, district, neighborhood) -> None:
        self.__name = name
        self.__city = city
        self.__email = email
        self.__gender = gender
        self.__street = street
        self.__avenue = avenue
        self.__district = district
        self.__date_birth = date_birth
        self.__nationality = nationality
        self.__phone_number = phone_number
        self.__neighborhood = neighborhood
        self.__identity_card = identity_card
        self.__cod = self.select()[0] + 1
        self.__cod_acount_access = self.select()[1] + 1

    def __insert_client_data__(self, user_name) -> None:
        cursor.execute(f"insert into client values({self.__cod}, '{self.__name}', '{self.__identity_card}','{self.__phone_number}', '{self.__email}', '{self.__date_birth}', '{self.__gender}', '{self.__nationality}', '{self.__city}', '{self.__district}', '{self.__avenue}', '{self.__neighborhood}', '{self.__street}', {self.__cod_acount_access});")
    
        obj2 = WorkerClient(user_name)
        obj2.insert(self.__cod)

    def __insert_acount_data__(self, acount_number) -> None:
        cursor.execute(f"insert into acount_access values({self.__cod}, {acount_number}, default, default, {self.__cod}, {self.__cod}, {self.__cod});")
    
    def __insert_transfer__(self) -> None:
        cursor.execute(f"insert into transfer values({self.__cod}, default, default, default, default);")

    def __inert_deposit__(self) -> None:
        cursor.execute(f"insert into deposit values({self.__cod}, default, default);")
    
    def __insert_widraw__(self) -> None:
        cursor.execute(f"insert into widraw values({self.__cod}, default, default);")

    def select(self) -> list:
        cursor.execute('select count(cod), count(cod_acount_access) from client;')

        vet = list()
        [vet.append(c) for cur in cursor for c in cur]
        return vet


class WorkerClient:
    def __init__(self, user) -> None:
        self.__user = user

    def insert(self, cod) -> None:
        cursor.execute(f'insert into add_client values({cod}, default, {cod}, {self.__select()})')

    def __select(self) -> int:
        cursor.execute(f'select w.cod from worker w join user u on u.cod_worker = w.cod where u.user_name = "{self.__user}"')
        vet = list()
        [vet.append(c) for cur in cursor for c in cur]
        [test := v for v in vet]

        return test
    