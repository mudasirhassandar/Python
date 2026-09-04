# create a new file practice.txt using the python
# file = open("practice.txt","w")
# file.write("hi everyone \nwe are learning file I/O\nusing JAVA\ni like programming in JAVA")

# WAP that replaces all occurance of JAVA with python in the same file
# file = open("practice.txt", "r")
# data = file.read()
# print(data)
# new_data = data.replace("JAVA", "PYTHON")
# print(new_data)


# search in the file if the learning word exists or not and also print the in which line word learning occures first
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as file:
        data = file.read()
    if word in data:
        print("Found ")
    else:
        print("Not found")


def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as file:
        while data:
            data = file.readline()
            if word in data:
                print("Line no. =", line_no)
                return
            line_no += 1


check_for_word()
check_for_line()
