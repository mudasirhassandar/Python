# -------READING THE FILE----------------
# file = open("demo.txt", "r")
# data = file.read() # read the text file
# data = file.read(5) # rading only first five latters
# line1 = file.readline()  # reads the first line only
# print(line1)
# line2 = file.readline()  # reads the second line only
# print(line2)
# print(type(data))
# file.close()

# ---------------WRITING IN THE FILE-------------

# file = open("demo.txt","w")
# file.write("Hello this new data")
# file.close()

# --------------APPEND THE DATA IN FILE-------------
# file = open("demo.txt","a")
# file.write("\nHello who are you")
# file.close()

# -----------CREATING THE NEW FILE-----------------
# file = open("videos.mp4","w")
# file.close()

# file = open("videos.mp4","a") #creating the new file
# file.close()

# file = open("demo.txt","r+") #overwrites at beginning
# file.write("hello world ")
# file.close()

# file = open("demo.txt","w+")
# file.write("hello i am mudasir")
# file.close()

# file = open("demo.txt", "a+")
# file.write(" hahahahhah")
# file.close()

# with open("demo.txt", "a+") as file:
#     data = file.read()
#     print(data)
#     file.close() #not important with will close file automatically

# -----------DELETING THE FILE----------------
# we use library for this->OS library
# import os
# os.remove("sample.txt")
