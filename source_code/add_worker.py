from funcionalitys import __Error_Handle__, worker_kinde_menu, __Error_Handle__
from validation import __valid_date__, __valid_name__, __valid_identity_card__, __valid_phone_number__
from add_client import CheckData

class Worker(CheckData):

    def __init__(self):
        super().__init__()
    
    def name(self) -> str:
        name = __valid_name__('Enter The Name: ')
        return name
    
    def number_identity(self) -> str:
        identity = __valid_identity_card__('Enter The Identity Number: ')
        if self.check_identity_card_client(identity) == True:
            __Error_Handle__(value=2, text='Identity_card allready Exists!')

        elif self.check_identity_card_worker(identity) == True:
            __Error_Handle__(value=2, text='Identity_card allready Exists!')
        else:
            return identity
    
    def phone_number(self) -> str:
        number = __valid_phone_number__('Enter the Phone Number: ')
        if self.check_phone_number(number) == True:
            __Error_Handle__(value=2, text='Phone Number allready Exists!')
        else:
            return number
        
    def worker_kind(self) -> str:
        function = worker_kinde_menu()
        match function:
            case 1:
                return 'grh'
            case 2:
                return 'normal worker'
            case _:
                __Error_Handle__(value=1, text='Invalid Option!')

    def date_birth(self) -> str:
        date_birth = __valid_date__('Enter The Date Birth: ')

        if self.check_age(date_birth) == False:
            __Error_Handle__(value=2, text='The Age Isn´t Anougth!')
        else:
            return date_birth

    def all_functions(self) -> None:
        pass
class Insert:
    pass
