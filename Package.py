class Package:
    def __init__(self, name):
        self.__name = name
        self.__desc = None
        self.__depencies = []
        self.__reverse_depencies = []
        self.__installed = False

    def __str__(self) -> str:
        return self.__name

    __repr__ = __str__

    def __lt__(self, other: object):
        return self.__name < other.get_name()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_desc(self):
        return self.__desc

    def set_desc(self, desc):
        self.__desc = desc

    def get_depencies(self):
        list_to_return = sorted(self.__depencies)
        return list_to_return

    def add_depency(self, depency: object):
        self.__depencies.append(depency)

    def get_reverse_depencies(self):
        list_to_return = sorted(self.__reverse_depencies)
        return list_to_return

    def add_reverse_depency(self, depency: object):
        self.__reverse_depencies.append(depency)

    def get_installed(self) -> bool:
        return self.__installed

    def set_installed(self):
        self.__installed = True