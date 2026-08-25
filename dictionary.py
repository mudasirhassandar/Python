# dict = {
#     "name": "mudasir",
#     "cgpa": 9.4,
#     "marks": [98, 78, 89],
# }
# print(dict)
# print(type(dict))
# print(dict["name"]) # printing only one key
# dict["name"] = "Hassan" #we can change the value of any key because its mutable
# print(dict)

# dict["Address"] = "Tral"  # Here we can add a new key in dictionary
# print(dict)

# Nested Dictionary
dict1 = {
    "Name": "Mudasir",
    "Roll_no": 72,
    "Score": {
        "Math": 98,
        "Chem": 96,
        "Phy": 92,
    },
}
# print(dict1)
# print(dict1["Score"]["Chem"]) #output = 96
# dict1["Score"]["Chem"] = 100  # changes the marks of chemistry from 96 to 100
# print(dict1)

# Dictionary Methods
print(dict1.keys())  # it gives me all the keys in dictionary
print(dict1.values())  # it gives me all the values of keys
print(dict1.items())  # it gives both keys and values
print(dict1.get("Score"))  # it gives only the score key and its values
dict1.update({"city": "Panner Jagir"})  # adds city and its value in dictionary
print(dict1.items())
