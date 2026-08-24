# WAP TO ASK THE USER TO ENTER THE NAME OF THEIR 3 FAVORITE SUBJECTS AND STORE THEM IN A LIST
# list = []
# list.append(input("Enter the First Subject : "))
# list.append(input("Enter the Second Subject : "))
# list.append(input("Enter the Third Subject : "))
# print("\nSubjects are:")
# print(list)

# WAP TO CHECK IF A LIST CONTAINS PALINDROME OF ELEMENTS

list = [1, 2, 3, 2, 1]
list1 = [1, 2, 3, 4, 5]

list_copy = list.copy()
list1_copy = list1.copy()
list_copy.reverse()
list1_copy.reverse()
if list == list_copy:
    print("List is palindrome")
else:
    print("List is not Palindrome")
if list1 == list1_copy:
    print("List1 is palindrome")
else:
    print("List1 is not Palindrome")

# WAP TO COUNT THE NUMBER OF STUDENTS WITH GRADE A
grades = ("A", "B", "C", "D", "A", "B", "A", "D", "C", "A", "A", "A")
print("Number of Students with Grade A =", grades.count("A"))

grades1 = ["A", "B", "C", "D", "A", "B", "A", "D", "C", "A", "A", "A"]
grades1.sort()
print(grades1)
