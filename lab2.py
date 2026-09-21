# dict = {"Name": "Mudasir", "RollNo": "CSE-24-72", "CGPA": 9.0}
# print(dict["Name"])
# dict["Name"] = "Mudasir Hassan"
# print(dict["Name"])
# print(dict["RollNo"])
# print(dict["CGPA"])


# -------nested dictionary------
# dict ={
#     "name":"inder",
#     "rollno":"cse-24-57",
#     "score":{
#         "phy":78,
#         "chem":90,
#         "math":87

#     }
# }
# print(dict["score"]["chem"])
# dict["score"]["chem"] = 100
# print(dict["score"]["chem"])

# ------methods of dictionary------
student = {"name": "Mudasir Ahmad Dar", "rollno": "cse-24-72"}
dict = {"cgpa": 9.0}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"Address": "Tral", "age": 20})
print(student)
student.update(dict)
print(student)
