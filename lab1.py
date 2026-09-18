# ----------list-------------


# thislist = ["apple","banana","mango"]
# print(thislist)
# print(len(thislist))
# thislist.append("orange")
# print(thislist)
# thislist.remove("apple")
# thislist.pop()
# print(thislist)

# items = ["laptop","mobile"]
# item = ["headphones"]
# items.extend(item)
# print(items)

# numbers = [1,4,2,5,7,4,2,8]
# print(numbers)
# print(numbers[0:4])
# print(numbers[-4:-1])
# print(numbers[3])
# numbers[3] = 10
# print(numbers)

# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# numbers.insert(0,11)
# print(numbers)
# numbers.remove(11)
# print(numbers)

# furits = ["banana","grapes","apple","orange"]
# furits.sort()
# print(furits)


# --------tuple---------

# thistuple = (67,34,23,67,12,11,78,67,90)
# print(len(thistuple))
# print(thistuple[2])
# print(type(thistuple))
# print(thistuple[2:5])

# print(thistuple.index(23))
# print(thistuple.count(67))


# ----------sets---------------


collection = {1, 2, 3, 4, 5, 56, 23, 34}
# print(type(collection))
# print(len(collection))
# print(collection)
# collection.add(64)
# print(collection)
# collection.add(44)
# print(collection)
# print(collection.pop())
collection.remove(2)
print(collection)
collection.discard(34)
print(collection)
collection.discard(10)

# thisset = set()
# thisset.add((2,3,4,5))
# print(thisset)

# set1 = {
#     2,
#     3,
#     1,
#     4,
#     5,
#     6,
# }
# set2 = {2, 3, 7, 43, 23, 10}
# print(set1.union(set2))
# print(set1.intersection(set2))
# set1.intersection_update(set2)
# print(set1)
