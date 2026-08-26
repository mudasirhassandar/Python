# WAF TO PRINT THE LENGTH OF A LIST (LIST IN THE PARAMETER)
# cities = ["tral", "pulwama", "panner", "mandoora", "awantipora", "aripal"]
# items = ["mobile", "laptop", "tab", "desktop"]


# def print_len(list):
#     print(len(list))


# print_len(cities)
# print_len(items)

# WAF TO PRINT THE LIST IN THE SINGLE LINE
# cities = ["tral", "pulwama", "panner", "mandoora", "awantipora", "aripal"]


# def print_list(list):
#     for item in list:
#         print(item, end=" ")


# print_list(cities)
# print()

# calculate the factorial


def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)


cal_fact(5)
cal_fact(6)
cal_fact(3)
cal_fact(8)
