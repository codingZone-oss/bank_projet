from funcionalitys import show_name, show_palet, show_palet2, worker_kinde_menu, __Error_Handle__, palete
from validation import __valid_date__, __valid_email__, __valid_name__, __valid_identity_card__, __valid_phone_number__, __valid_local_name__, __valid_user_name__, __valid_password__, __valid_answerd__
from add_client import CheckData
from conextion_mysql import cursor

class Worker(CheckData):

    def __init__(self, admin_name):
        super().__init__()
        self.__adm_name = admin_name
    
    def name(self) -> str:
        name = __valid_name__('Enter The Name: ')
        return name
    
    def user_name(self) -> str:
        while True:
            tester = 0
            obj = UserSql()
            user_name = __valid_user_name__('Enter The User Name: ')
            [tester := 1 for v in obj.select() if user_name == v]
            if tester == 1:
                __Error_Handle__(value=1, text='User Name allread Exist: ')
                continue
            else:
                return user_name

    def password(self) -> str:
        while True:
            tester = 0
            obj = UserSql()
            password = __valid_password__('Enter The Password: ')
            [tester := 1 for v in obj.select() if password == v]
            if tester == 1:
                __Error_Handle__(value=1, text='Password allread Exist: ')
                continue
            else:
                return password

    def number_identity(self) -> str:
        while True:
            identity = __valid_identity_card__('Enter The Identity Number: ')
            if self.check_identity_card(identity, 'worker') == True:
                __Error_Handle__(value=1, text='Identity_card allready Exists!')
                continue

            elif self.check_identity_card(identity, 'client') == True:
                __Error_Handle__(value=1, text='Identity_card allready Exists!')
                continue
            else:
                return identity
    
    def phone_number(self) -> str:
        while True:
            number = __valid_phone_number__('Enter the Phone Number: ')
            if self.check_phone_number(number, 'worker') == True:
                __Error_Handle__(value=1, text='Phone Number allready Exists!')
                continue
            else:
                return number
        
    def worker_kind(self) -> str:
        while True:
            palete()
            function = worker_kinde_menu()
            match function:
                case 1:
                    return 'grh'
                case 2:
                    return 'normal worker'
                case _:
                    __Error_Handle__(value=1, text='Invalid Option!')

    def date_birth(self) -> str:
        while True:
            date_birth = __valid_date__('Enter The Date Birth: ')

            if self.check_age(date_birth) == False:
                __Error_Handle__(value=1, text='The Age Isn´t Anougth!')
                continue
            else:
                return date_birth

    def email(self) -> str:
        while True:
            email = __valid_email__('Enter The Email: ')

            if self.check_email(email, 'worker') == True:
                __Error_Handle__(value=1, text='Email allready Exists!')
                continue
            else:
                return email
            
    def complements(self) -> list:
        nationality = __valid_local_name__('Enter The Nationality: ')
        city = __valid_local_name__('Enter The City: ')
        avenue = __valid_local_name__('Enter The Avenue: ')
        street = __valid_local_name__('Enter The Street: ')
        district = __valid_local_name__('Enter The District: ')
        neighborhood = __valid_local_name__('Enter The Neighborhood: ')
        vet = [nationality, city, avenue, street, district, neighborhood, ]

        return vet

    def all_function(self) -> None:
        show_name(self.__adm_name, 'Adminstrator')
        show_palet2('Adding a New Worker')
        show_palet('Personal Data')
        name = self.name()
        identity = self.number_identity()
        phone = self.phone_number()
        birth = self.date_birth()
        kind = self.worker_kind()
        email = self.email()
        show_palet('Address Data')
        complements = self.complements()

        answ = __valid_answerd__('Also Creat a New User for this Worker [Y:N]: ')
        obj = WorkerSql()
        obj.insert(name, identity, phone, birth, kind, email, complements)
        
        if answ == 'y':
            user_name = self.user_name()
            password = self.password()
            obj = UserSql()
            obj.insert(user_name, password) 
        
        show_palet2(f'{kind.upper()} {name.capitalize()} Added with Success!')

class WorkerSql:

    def select1(self) -> list:
        cursor.execute(f'select count(cod) from user')
        vet = list()
        [vet.append(c) for cur in cursor for c in cur]
        return vet
    
    def select2(self) -> list:
        cursor.execute(f'select count(cod) from worker')
        vet = list()
        [vet.append(c) for cur in cursor for c in cur]
        return vet

    def insert(self, name, identity, phone, birth, kind, email, complements, ) -> None:
        cursor.execute(f"insert into worker values({self.select2()[0]+1}, '{name}', '{identity}', '{kind}', '{birth}', '{phone}', '{email}', '{complements[0]}', '{complements[1]}', '{complements[4]}', '{complements[2]}', '{complements[5]}', '{complements[3]}', default);")

class UserSql(WorkerSql):

    def select(self) -> list:
        cursor.execute("select user_name, pass_word from user")
        vet = list()
        [vet.append(cur) for line in cursor for cur in line]
        return vet
    
    def insert(self, user_name:str, password:str) -> None:
        cursor.execute(f"insert into user values ({self.select1()[0]+1}, '{user_name}', '{password}', '{self.select2()[0]}')")
