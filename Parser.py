from io import TextIOWrapper
from Package import Package

class TOML_Parser:
    def __init__(self, filename: str):
        self.__data = self.parse_TOML(filename)

    def parse_TOML(self, filename: str):
        file = open(filename, "r")

        if not self.is_toml(file):
            return 

        to_return = self.get_installed_packages(file)

        self.populate_packages_with_depencies(to_return, file)
        
        file.close()
        return to_return
    
    def is_toml(self, file: TextIOWrapper):
        try:
            file.read()
            return True
        except UnicodeDecodeError:
            return False

    def get_installed_packages(self, file: TextIOWrapper):
        file.seek(0)
        package = False
        to_return = {}

        for line in file:
            text = line.strip()

            if len(text) == 0:
                continue

            elif "[metadata]" in text:
                break

            elif "[[package]]" in text:
                package = True

            elif "[package." in text:
                package = False

            elif package:
                if "name" in text:
                    name = text.split('"')[1].lower()
                    if to_return.get(name) == None:
                        p = Package(name)
                        p.set_installed()
                        to_return[name] = p
                    name_to_store = name

                elif "description" in text:
                    desc = text.split('"')[1]
                    p = to_return[name_to_store]
                    p.set_desc(desc)
                    
        return to_return
    
    def populate_packages_with_depencies(self, data: dict, file: TextIOWrapper):
        file.seek(0)
        depencies = False
        package = False
        name_to_store = None

        for line in file:
            text =  line.strip()

            if len(text) == 0:
                continue

            elif "[metadata]" in text:
                break

            elif "[[package]]" in text:
                package = True
                depencies = False

            elif "[package." in text:
                package = False
                depencies = True

            elif package:
                if "name" in text:
                    name_to_store = text.split('"')[1].lower()

            elif depencies:
                splitted = text.split("=", 1)
                skipped_depencies = ["testing", "docs", "tests", "tests_no_zope", "perf"]
                
                if(splitted[0].strip() == "dev"):
                    for entry in splitted[1].split(','):
                        dep_name = entry.split('"')[1].split("(")[0].strip().lower()

                        self.solve_depencies(data, name_to_store, dep_name)

                elif(splitted[0].strip() not in skipped_depencies):
                    dep_name = splitted[0].strip().lower()

                    self.solve_depencies(data, name_to_store, dep_name)

    def solve_depencies(self, data, pack_name, dep_name):
        p = data[pack_name]

        # Add depencies to packages that are already installed
        if(data.get(dep_name) != None):
            p2 = data[dep_name]
            p2.add_reverse_depency(p)
            p.add_depency(p2)

        # Add depencies to packages that are not installed
        else:
            p2 = Package(dep_name)
            p2.add_reverse_depency(p)
            p.add_depency(p2)

    def get_data(self):
        return self.__data
        
