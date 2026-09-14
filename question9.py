# create a student class that takes name and maeks of 3 subjects as arguments in constructor
# then create a method to print the average


class Students:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        subjects = 0
        for val in self.marks:
            sum += val
            subjects += 1
        return sum / subjects

    @staticmethod  # Static method .without self parameter
    def hello():
        print("Hello I am Your host")


s1 = Students("Mudasir", [100, 100, 100])
print(s1.name)
print(s1.marks)
print(f"Average Maeks:{s1.average():.2f}")
s1.hello()
