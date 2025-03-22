from Model.Places import Place
from Model.Users import User
from Model.Amenities import Amenity
from Model.Reviews import Review


class PlaceManagement:
    def __init__(self, place_instance: Place):
        self.place = place_instance

    def add_host(self, host: User):
        if len(self.place.host_id) == 0:
            self.place.host_id.append(host.object_id)
            return self.place.host_id
        else:
            return "The place has already host"

    def change_host(self, new_host: User):
        if len(self.place.host_id) == 1:
            self.place.host_id[0] = new_host.object_id
            return "New host is added successfully"
        elif self.place.host_id == 0:
            self.add_host(new_host.object_id)
            return "New host is added successfully"

    def add_amenity_to_place(self, amenity: Amenity):
        if amenity.object_id not in self.place.amenities:
            self.place.amenities.append({amenity.object_id: amenity.amenity_name})
            return "Amenity is added successfully"
        return "Amenity is already exists in Place"

    def add_review_to_place(self, user: User, review: Review):
        self.place.reviews.append({user.first_name: review.user_comment})
        return "Review is added successfully"
