"""
Reaktor Fall 2022 Software developer trainee
Preliminary Assignment

This module defines a class named Package, which is used to demonstrate a 
projects depency package
"""
class Package:
    """Class defines a Package and its methods"""

    def __init__(self, name):
        """Constructor to initialize a package"""
        self.__name = name
        self.__desc = None
        self.__depencies = []
        self.__reverse_depencies = []
        self.__installed = False

    def __str__(self) -> str:
        """Method for representing the object as a string"""
        return self.__name

    # represents the object as a string in lists etc
    __repr__ = __str__

    def __lt__(self, other: object):
        """Method to compare a package to another package for sorting purposes"""
        return self.__name < other.get_name()

    def get_name(self) -> str:
        """Getter for the name of the depency package"""
        return self.__name

    def set_name(self, name: str):
        """Setter for the name of the depency package"""
        self.__name = name

    def get_desc(self) -> str:
        """Getter for the description of the depency package"""
        return self.__desc

    def set_desc(self, desc: str):
        """Setter for the description of the depency package"""
        self.__desc = desc

    def get_depencies(self) -> list:
        """Getter for the depencies of the depency package"""
        list_to_return = sorted(self.__depencies)
        return list_to_return

    def add_depency(self, depency: object):
        """Method adds a depency for the package"""
        self.__depencies.append(depency)

    def get_reverse_depencies(self) -> list:
        """Getter for the reverse depencies of the package"""
        list_to_return = sorted(self.__reverse_depencies)
        return list_to_return

    def add_reverse_depency(self, depency: object):
        """Method adds a reverse depency for the package"""
        self.__reverse_depencies.append(depency)

    def get_installed(self) -> bool:
        """Getter the see if the depency is installed or not"""
        return self.__installed

    def set_installed(self):
        """Sets the depency package as an installed package"""
        self.__installed = True
