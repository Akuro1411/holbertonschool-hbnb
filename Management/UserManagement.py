from Model.Users import User
from Model.Places import Place
from Model.Reviews import Review
from Management.PlaceManagement import PlaceManagement


class UserManagement:
    def __init__(self, user: User):
        self.user = user

    def own_new_place(self, place: Place):
        self.user.owned_places.append({place.object_id: place.name})
        place_manage = PlaceManagement(place)
        if not self.user.is_owner and len(place.host_id) == 0:
            place_manage.add_host(self.user)
            self.user.is_owner = True
        else:
            place_manage.change_host(self.user)

    def write_review(self, place: Place, rate, comment):
        new_review = Review(self.user.object_id, place.object_id, rate, comment)
        place_manage = PlaceManagement(place)
        result = place_manage.add_review_to_place(self.user, new_review)
        return result
