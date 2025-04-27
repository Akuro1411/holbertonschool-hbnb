from Persistance.IPersistance import IPersistenceManager


class DataManager(IPersistenceManager):
    def __init__(self):
        self.data_dict = {"Place": {}, "User": {}, "Amenity": {}, "Review": {}, "City": {}, "Country": {}}

    def save(self, entity):
        entity_type = entity.__class__.__name__
        self.data_dict[entity_type][str(entity.object_id)] = entity.__dict__
        return f"{entity_type} is saved successfully"

    def get(self, entity_id, entity_type):
        return self.data_dict[entity_type][str(entity_id)]

    def update(self, entity):
        entity_type = entity.__class__.__name__
        self.data_dict[entity_type][str(entity.object_id)] = entity.__dict__
        return "Entity is updated successfully"

    def delete(self, entity_id, entity_type):
        del self.data_dict[entity_type][str(entity_id)]
        return "Entity is deleted successfully"
