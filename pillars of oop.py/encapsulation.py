class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

        #  accessor
    def get_name(self): 
        return self.__name
        # print "{self.__name}"

        # mutator
    def set_name(self, name):
        self.__name = name
p=Person("samia", 23)
p.get_name();
