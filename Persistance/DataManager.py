import json
from Persistance.IPersistance import IPersistenceManager
from Model.Users import User


class DataManager(IPersistenceManager):
    def __init__(self):
        self.data_dict = {"Place": {}, "User": {}, "Amenity": {}, "Review": {}, "City": {}, "Country": {}}
    def save(self, entity):
        entity_type = entity.__class__.__name__
        self.data_dict[entity_type][entity.object_id] = entity
        return f"{entity_type} is saved successfully"

    def get(self, entity, entity_id):
        entity_type = entity.__class__.__name__
        return f"Here you are: {self.data_dict[entity_type][entity_id]}"


new_user = User("Nahid", "Isayev", "nahid@gmail.com", "1234")
data = DataManager()
data.save(new_user)
print(data.get(new_user, new_user.object_id))
