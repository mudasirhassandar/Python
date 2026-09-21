# ITS IS ALSO KNOWN AS OPERATOR OVERLOADING
# print(1 + 2)  # addition
# print("hello" + "world")  # concatenation
# print([1, 2, 3] + [4, 5, 6])  # merge


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real, "i +", self.img, "j")

    # def add(self, num2):
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     return Complex(newReal, newImg)
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)


num1 = Complex(2, 3)
num1.show()

num2 = Complex(6, 8)
num2.show()

# num3 = num1.add(num2)
num3 = num1 + num2
num3.show()
