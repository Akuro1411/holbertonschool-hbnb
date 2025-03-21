from Model.Interface import Interface
from validate_email import validate_email


class User(Interface):
    def __init__(self, firstname, lastname, user_mail, password, owner=False):
        super().__init__()
        self.first_name = firstname
        self.last_name = lastname
        if validate_email(user_mail):
            self.email = user_mail
        else:
            raise ValueError("Email is not valid")
        self.user_password = password
        self.is_owner = owner
        self.owned_places = []
