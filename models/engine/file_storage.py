#!/usr/bin/python3
"""
A Storage Engine based on file storage mechanisim and the JSON format.
This model is used to create a presistent copy of all the BnB models objects
in the form of a json file
"""
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
    """
    Syntax:
        FileStorage()

    Description:
        Creates a presistent copy of the BnB models objects in the form of
        json file

        FileStorage.all(self):
            returns a dicitionery consists of all the objects of the Bnb models
        FileStorage.new(self, obj):
            Update the objects dictionery with the
            <obj.__class__.__name__>.<obj.id> as the key
            and obj.to_dict() as its value

        FileStorage.save(self):
            Serializes the objects dictionery to a JSON file

        FileStorage.reload(self):
            Deserializes the JSON file to the objects dictionery
    """

    __file_path = os.path.join(os.path.dirname(__file__), 'file.json')
    __objects = {}

    def all(self):
        """
        all    return a dictionery consists of all the objects instances of
               the BnB models

        Syntax:
            FileStorage.all()

        Return:
            A dictionery contains BnB models instances
        """

        return self.__objects

    def new(self, obj):
        """
        new    add the obj information to the BnB objects dictionery

        Syntax:
            FileStorage.new(self, obj)
        """

        key = obj.to_dict()['__class__'] + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        save   save the BnB objects dictionery into a JSON file

        Syntax:
            FileStoarge.save()

        Descriptons:
            `save` saves all the BnB objects instances to a JSON file, in the
             form of json key:value pairs.
             If the file dose not exists the `save` will creates a new one, if
             it's already exist it will be over-written
        """

        with open(self.__file_path, 'w') as f:
            data = {key: val.to_dict() for key, val in self.__objects.items()}
            json.dump(data, f)

    def reload(self):
        """
        reload    load the contents of the json file to the BnB objects
                  instances dictionery

        Syntax:
            FileStorage.load()

        Descriptions:
            `reload` get the contents of the json file and converts them into
             python dictionery, and the value of the BnB objects instances
             dictionery will be updated with it.
        """

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
