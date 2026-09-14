# 3) Inheritance -> One class can derives properties and methods from another class.
#     Parent class ---> Child class


# class Car:  # parent class
#     color = "Black"

#     @staticmethod
#     def start_car():
#         print("Car is Started..")

#     @staticmethod
#     def stop_car():
#         print("Car Stop..")


# class toyotacar(Car):  # child class
#     def __init__(self, name):
#         self.name = name


# car1 = toyotacar("Fortuner")
# print(car1.name)
# print(car1.color)
# print(car1.start_car())
# print(car1.stop_car())


# -------Types of Inheritance-----
# 1) single inheritance


# class A:
#     varA = "Hello i am mudasir"


# class B(A):
#     varB = "I am learning python"


# variable = B
# print(variable.varA)
# print(variable.varB)

# 2) Multi-Level inheritance


# class A:
#     varA = "Hello i am mudasir"


# class B(A):
#     varB = "I am learning python"


# class C(B):
#     varC = "I am in 5th sem"


# variable = C
# print(variable.varA)
# print(variable.varB)
# print(variable.varC)


# 2) Multiple inheritance


# class A:
#     varA = "Hello i am mudasir"


# class B:
#     varB = "I am learning python"


# class C(A, B):
#     varC = "I am in 5th sem"


# variable = C
# print(variable.varA)
# print(variable.varB)
# print(variable.varC)


# --------Super Method---------


class Car:  # parent class
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start_car():
        print("Car is Started..")

    @staticmethod
    def stop_car():
        print("Car Stop..")


class toyotacar(Car):  # child class
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start_car()


car1 = toyotacar("fortuner", "Petrol")
print(car1.name)
print(car1.type)
