# 1) Abstraction -> Hidding the unnecessary data


# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car Started...")


# car1 = Car()
# car1.start()


# 2) Encapsulation -> Wrapping data and functions into a single unit(object)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def hello(self):
#         print("Hello", self.name)

#     def get_Marks(self):
#         return self.marks


# s1 = Student("Mudasdir Hassan", 97)
# s1.hello()
# print(s1.get_Marks())


# --------del Keyword -> used for delete the object or attributes of object


# class Student:
#     def __init__(self, name):
#         self.name = name


# s1 = Student("Mudasir")
# print("1->", s1)
# del s1.name
# print("2->", s1)
# del s1
# print("3->", s1)


# ------private Attributes-------
# class Account:
#     def __init__(self, acc, password):
#         self.account_number = acc
#         self.__password = password  # private data

#     def show_password(self):
#         print(self.__password)


# acc1 = Account(3160, 6786)
# print(acc1.account_number)
# print(acc1.show_password())
