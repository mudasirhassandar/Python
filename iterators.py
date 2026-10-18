numbers = [2, 5, 1, 7, 4]
# for i in numbers:
#     print(i) #prints all the list once automatically

mudasir = iter(numbers)  # creates the iterator from the numbers
try:
    print(next(mudasir))
    print(next(mudasir))  # print elements one by one
    print(next(mudasir))
    print(next(mudasir))
    print(next(mudasir))
    print(next(mudasir))
except StopIteration:
    print("No more elements")
