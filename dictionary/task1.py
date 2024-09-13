student_dict = {
    "101": "Alice",
    "102": "Bob",
    "103": "Charlie",
    "104": "David",
    "105": "Eve"
}

student_dict["106"] = "Frank"
print(student_dict)

student_dict["102"] = "Bob Smith"
print(student_dict)

name = student_dict["103"]
print(name)

nested_dict = {
    "class1": {
        "101": "Alice",
        "102": "Bob"
    },
    "class2": {
        "103": "Charlie",
        "104": "David"
    }
}

name = nested_dict["class1"]["101"]
print(name)

keys = student_dict.keys()
print(keys)

del student_dict["105"]
print(student_dict)