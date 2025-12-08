from add_worker import UserSql, WorkerSql
from funcionalitys import __Error_Handle__, palete, show_palet, show_palet2, worker_kinde_menu
from validation import __valid_answerd__, __valid_date__, __valid_email__, __valid_identity_card__, __valid_local_name__, __valid_name__, __valid_password__, __valid_phone_number__, __valid_user_name__
from add_client import CheckData
from conextion_mysql import cursor

class NewsData(CheckData):

    def __init__(self, old_name):
        super().__init__()
        self.old_name = old_name
    
    def select(self, name) -> list:
        cursor.execute(f"select cod, name_worker, number_identity_card, funtion_type, date_birth, phone_number, email, nacionality, city, district, avenue, neighborhood, street from worker where name_worker = '{name}' limit 1;")

        vet = list()
        [vet.append(c) for cur in cursor for c in cur]
        return vet
    
    def select_user(self, cod) -> list:
        cursor.execute(f"select u.user_name, u.pass_word from user u join worker w on w.cod = u.cod_worker where u.cod = '{cod}' limit 1;")

        vet = list()
        [vet.append(c) for cur in cursor for c in cur]
        return vet


    def new_name(self) -> str:
        name = __valid_name__('Enter The New Name or ENTER to Keep: ', True)
        if not name:return str(self.old_name)
        return name
        

    def new_number_identity(self) -> str:
        while True:
            identity = __valid_identity_card__('Enter The New Identity Number or ENTER to Keep: ', True)
            if not identity:return str(self.select(self.old_name)[2])

            if self.check_identity_card(identity, 'worker') == True:__Error_Handle__(value=1, text='Identity_card allready Exists!');continue

            elif self.check_identity_card(identity, 'client') == True:__Error_Handle__(value=1, text='Identity_card allready Exists!');continue
            else:return identity


    def new_phone_number(self) -> str:
        while True:
            number = __valid_phone_number__('Enter the New Phone Number or ENTER to Keep: ', True)
            if not number:return str(self.select(self.old_name)[5])

            if self.check_phone_number(number, 'worker') == True:
                __Error_Handle__(value=1, text='Phone Number allready Exists!')
                continue
            else:
                return number


    def new_worker_kind(self) -> str:
        while True:
            palete()
            function = worker_kinde_menu()
            if not function:return str(self.select(self.old_name)[3])
            match function:
                case 1:return 'grh'
                case 2:return 'normal worker'
                case _:__Error_Handle__(value=1, text='Invalid Option!')


    def new_date_birth(self) -> str:
        while True:
            date_birth = __valid_date__('Enter The Date Birth: ', True)
            if not date_birth:return str(self.select(self.old_name)[4])

            if self.check_age(date_birth) == False:
                __Error_Handle__(value=1, text='The Age Isn´t Anougth!')
                continue
            else:
                return date_birth


    def new_email(self) -> str:
        while True:
            email = __valid_email__('Enter The Email: ', True)
            if not email:return str(self.select(self.old_name)[6])

            if self.check_email(email, 'worker') == True:
                __Error_Handle__(value=1, text='Email allready Exists!')
                continue
            else:
                return email
            

    def new_complements(self) -> list:
        nationality = __valid_local_name__('Enter The Nationality: ', True)
        if not nationality:nationality = str(self.select(self.old_name)[7])

        city = __valid_local_name__('Enter The City: ', True)
        if not city:city = str(self.select(self.old_name)[8])
        
        avenue = __valid_local_name__('Enter The Avenue: ', True)
        if not avenue:avenue = str(self.select(self.old_name)[10])

        street = __valid_local_name__('Enter The Street: ', True)
        if not street:street = str(self.select(self.old_name)[12])

        district = __valid_local_name__('Enter The District: ', True)
        if not district:district = str(self.select(self.old_name)[9])

        neighborhood = __valid_local_name__('Enter The Neighborhood: ', True)
        if not neighborhood:neighborhood = str(self.select(self.old_name)[11])

        vet = [nationality, city, district, avenue, neighborhood, street,]
        return vet
    

    def new_user_name(self) -> str:
        while True:
            tester = 0
            obj = UserSql()
            user_name = __valid_user_name__('Enter The User Name: ', True)
            if not user_name:return str(self.select_user(self.select(self.old_name)[0])[0])

            [tester := 1 for v in obj.select() if user_name == v]
            if tester == 1:__Error_Handle__(value=1, text='User Name allread Exist: ');continue
            else:return user_name


    def new_password(self) -> str:
        while True:
            tester = 0
            obj = UserSql()
            password = __valid_password__('Enter The Password: ', True)
            if not password:return str(self.select_user(self.select(self.old_name)[0])[1])

            [tester := 1 for v in obj.select() if password == v]
            if tester == 1:__Error_Handle__(value=1, text='Password allread Exist: ');continue
            else:return password


    def all_function(self) -> None:
        show_palet2('Updating Worker')
        show_palet('Personal Data')
        new_name = self.new_name()
        new_identity = self.new_number_identity()
        new_phone = self.new_phone_number()
        new_birth = self.new_date_birth()
        new_kind = self.new_worker_kind()
        new_email = self.new_email()
        show_palet('Address Data')
        new_complements = self.new_complements()

        answ = __valid_answerd__('Also Update the New User for this Worker [Y:N]: ')
        obj = WorkerSql()
        obj.update(self.select(self.old_name)[0], new_name, new_identity, new_phone, new_birth, new_kind, new_email, new_complements)
        
        if answ == 'y':
            new_user_name = self.new_user_name()
            new_password = self.new_password()
            obj = UserSql()
            obj.update(self.select(self.old_name)[0], new_user_name, new_password) 
        
        show_palet2(f'{new_kind.upper()} {new_name.capitalize()} Updated with Success!')

# obj = NewsData('new name')
# print(obj.new_password())