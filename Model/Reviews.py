# Each review will be separate object, and it will have relation with places and users.
from Model.Interface import Interface


class Reviews(Interface):
    def __init__(self, user, place, rate, comment):
        super().__init__()
        self.user_id = user
        self.place_id = place
        self.rating = rate
        self.user_comment = comment
