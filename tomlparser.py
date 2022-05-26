"""
Reaktor Fall 2022 Software developer trainee
Preliminary Assignment

This module defines a parser, which is used to parse user uploaded files
to visualizable form. Uses the Package.class to demonstrate a single depency.
"""
from io import TextIOWrapper
from package import Package

class TomlParser:
    """Class defines the parser and its methods for parsing the file"""

    def __init__(self, filename: str):
        """Constructor to initialize the parser, parses the file in initialize"""
        self.__data = self.parse_TOML(filename)

    def parse_TOML(self, filename: str) -> dict:
        """Method for parsing the file, returns a dict with the data of the procjets
        depencies
        """
        file = open(filename, "r")

        if not self.is_toml(file):
            return 

        to_return = self.get_installed_packages(file)

        self.populate_packages_with_depencies(to_return, file)
        
        file.close()
        return to_return
    
    def is_toml(self, file: TextIOWrapper) -> bool:
        """Method for checking that the given file is atleast a text file"""
        try:
            file.read()
            return True
        except UnicodeDecodeError:
            return False

    def get_installed_packages(self, file: TextIOWrapper) -> dict:
        """Populates the database with installed packages"""
        file.seek(0)
        package = False
        to_return = {}

        for line in file:
            text = line.strip()

            if len(text) == 0:
                continue

            # We are not interested in the metadata of the poetry.lock files.
            # These are located in the bottom of the file, so if we reach the [metadata]
            # headline, we can stop parsing
            elif "[metadata]" in text:
                break

            # When we find a line with [[package]] we know that the next lines will
            # contain information about a depency package
            elif "[[package]]" in text:
                package = True

            # Lines after the [package.] contain depency information of the package
            #  and we are not interested in those at the moment
            elif "[package." in text:
                package = False

            # Make a Package.class from the depency information
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
        """Method to populate the installed packages in the database with depencies
        and reverse depencies
        """
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

            # If we find a package, save the name, so we know which package we
            # are populating with depencies
            elif package:
                if "name" in text:
                    name_to_store = text.split('"')[1].lower()

            # Add the depencies to the stored package, the depencies can be found in
            # different places so check them all. Only get the "dev" depencies for
            # the package. IF we want to include the "testing", "docs" etc packages 
            # which are now in the "skipped_depencies" list, take them out of the list.
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

    def solve_depencies(self, data: dict, pack_name: str, dep_name: str):
        """Method for solving the depencies of the packages"""
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

    def get_data(self) -> dict:
        """Getter for the parsed data"""
        return self.__data
        
