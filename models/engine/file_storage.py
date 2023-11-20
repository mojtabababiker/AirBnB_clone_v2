import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = os.path.join(os.path.dirname(__file__), 'file.json')
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.to_dict()['__class__'] + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            data = {key: val.to_dict() for key, val in self.__objects.items()}
            json.dump(data, f)

    def reload(self):
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val.get('__class__')
                    if class_name in classes:
                        self.__objects[key] = classes[class_name](**val)
        except FileNotFoundError:
            pass
