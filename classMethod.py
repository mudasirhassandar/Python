class Person:
    name = "Hassan"

    # def changeName(self, name):
        # self.name = name  # this is not the same name as above this name is different
        # Person.name = name  #this is one method
        # self.__class__.name = name  # this is another method
    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("Mudasir")
print(p1.name)
print(Person.name)
