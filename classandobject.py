# # Name of the students
# class Student:
#     name = "Mudasir Hassan"


# s1 = Student()
# print(s1.name)


# # Color of the cars
# class Cars:
#     color = "Green"


# car1 = Cars()
# print(car1.color)
# car2 = Cars()
# print(car2.color)
# car3 = Cars()
# print(car3.color)


# ---------CONSTRUCTOR---------
# class Student:
#     def __init__(self):  # Default constructor
#         pass

#     def __init__(self, name, marks):  # parameterized constructor
#         self.name = name
#         self.marks = marks
#         print("new student is added")
#         # print(self)


# s1 = Student("Mudasir", 87)
# print(s1.name)
# print(s1.marks)
# s2 = Student("Soriya", 76)
# print(s2.name)
# print(s2.marks)

# -------------Attributes------------
# class attributes , object attributes
# class Students:
#     collegename = "Iust" #class attribute

# s1 = Students()
# print(s1.collegename)

# ------Methods---------


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def hello(self):
        print("Hello", self.name)

    def get_Marks(self):
        return self.marks


s1 = Student("Mudasdir Hassan", 97)
s1.hello()
print(s1.get_Marks())
