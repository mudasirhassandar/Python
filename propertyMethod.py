class Student:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
        # self.percentage = str((self.phy + self.che + self.math) / 3) + "%"

    # def claculateAvg(self):
    #     self.percentage = str((self.phy + self.che + self.math) / 3) + "%"
    @property
    def percentage(self):
        return str((self.phy + self.che + self.math) / 3) + "%"


stu1 = Student(98, 78, 80)
print(stu1.percentage)

stu1.phy = 8
# print(stu1.phy)
# stu1.claculateAvg()
print(stu1.percentage)
