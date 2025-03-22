from Model.Interface import Interface
from Validation.UserValidation import email_validation


class User(Interface):
    def __init__(self, firstname, lastname, user_mail, password=None, owner=False):
        super().__init__()
        self.first_name = firstname
        self.last_name = lastname
        self.email = email_validation(user_mail)
        self.user_password = password
        self.is_owner = owner
        self.owned_places = []
