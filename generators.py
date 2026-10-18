def numbers(n):
    for i in range(1, n + 1):
        yield i


n = numbers(10)
try:
    while True:
        print(next(n))
except StopIteration:
    print("No elements Left")
