# collection = {1,2,3,4,"Mudasir",9.3}
# print(collection)
# print(type(collection))

# set1 = {1,2,2,3,4,5,5}
# print(set1)   #In output we will not see the repeated values or ignores the duplicate values
# print(type(set1))
# print(len(set1)) # give the length of set

# -------- creation of empty set ------------
# collection = {} ->this is the empty dictionary
# collection = set()  # this is the empty set
# print(type(collection))


# -----------SET METHODS----------------
# collection = set()
# collection.add("mudasir")  # adds the element in set
# collection.add("56.8")  # adds the element in set
# collection.add((92, 34, 32))  # adds the element in set
# print(collection)
# collection.remove("mudasir")
# collection.discard("mudasir")
# print(collection)  # removes the element from set
# collection.clear()  # Emptise the set
# print(collection)
# collection.pop() # Removes any random value from the set,so we do not use this
# print(collection)

set1 = {1, 2, 3, 4, 5, 5, 6}
set2 = {"mudasir", "computer", "python"}
set3 = set1.union(set2)  # combines the set1 and set2
print(set3)

set4 = {56, 2, 4, 34, 21, 67, 1}
set5 = set1.intersection(set4)  # Gives the common elements of both the sets
print(set5)
