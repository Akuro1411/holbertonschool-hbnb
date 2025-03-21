from abc import ABC
from uuid import uuid4
from datetime import datetime


class Interface(ABC):
    def __init__(self):
        self.object_id = uuid4()
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def update_date(self):
        self.update_at = datetime.now()
