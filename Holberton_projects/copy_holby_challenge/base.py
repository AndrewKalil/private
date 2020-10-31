#!/usr/bin/python3
""""""
import json
class Base():
    EXP_N_L = 10
    C_EXP = 0
    T_EXP = 0
    Level = 1
    S_Points = 0
    nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.nb_object += 1
            self.id = Base.nb_object
        self.C_EXP = Base.C_EXP
        self.T_EXP = Base.T_EXP
        self.Level = Base.Level
        self.S_Points = Base.S_Points
        self.EXP_N_L = Base.EXP_N_L

    @staticmethod
    def from_json_string(json_string):
        """converts json string to object

        Args:
            json_string (str): string representation of object

        Returns:
            object: object representation of json string
        """
        if json_string is None or len(json_string) is 0:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(dictionary):
        """converts object to json string

        Args:
            dictionary (object): object to be coverted

        Returns:
            str: string representation
        """
        if dictionary is None:
            return "[]"
        else:
            return json.dumps(dictionary, indent=4)

    @classmethod
    def load_from_file(cls, name):
        """loads a dictionary from a file and converts it to an instance

        Returns:
            object: new object that was created from dict in file
        """
        with open("{}.json".format(name)) as fd:
            obj = fd.read()
        return json.loads(obj)
