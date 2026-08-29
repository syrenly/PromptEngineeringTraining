# dictionary is a collection of key-value pairs. Each key is unique and meaningful, and it maps to a specific value.
# Dictionaries are mutable, meaning you can add, remove, or change key-value pairs after the dictionary has been created.

student = {
    "name": "John Doe",
    "age": 20,
}

marks = {
    1: 85,
    2: 90,
    3: 78,
}

status = {
    "is_enrolled": True,
    "is_graduated": False,
}

# accessing values using keys
print("Student name:", student["name"])

# accessing values using the get() method, which returns None if the key is not found instead of raising an error
print("Student age:", student.get("age"))
print(
    "Student grade:", student.get("grade", "Not available")
)  # default value if key not found

# update existing value
student["age"] = 21  # updating the value for the key "age"
print("Updated student age:", student["age"])

# adding a new key-value pair
student["grade"] = "A"  # adding a new key-value pair
print("Student grade after adding:", student["grade"])

# removing a key-value pair
student.pop("grade")  # removing the key-value pair with key "grade"
print("Student dictionary after removing grade:", student)

# print all the keys in the dictionary
print("Keys in student dictionary:", student.keys())

# print all the values in the dictionary
print("Values in student dictionary:", student.values())

for key in student:  # iterating through the dictionary keys
    print("Key:", key)

for value in student.values():  # iterating through the dictionary values
    print("Value:", value)

for key, value in student.items():  # iterating through the dictionary
    print(f"Key: {key}, Value: {value}")
