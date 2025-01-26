# Write a Python script that creates a dictionary to store information about three students 
# (name, age, and grade) and prints each student's information in a readable format. 
# Test Script: Include a sample dictionary in your script.

# Output Example:

# Name: John, Age: 20, Grade: A Name: Jane, Age: 22, Grade: B Name: Alice, Age: 19, Grade: A

student1 = {"Name":"Ralph", "Age":16, "Grade":"B"}
student2 = {"Name": "Steph", "Age": 15, "Grade": "D"}
student3 = {"Name": "John", "Age": 18, "Grade": "A"}

students = {
    "student1" : student1,
    "student2" : student2,
    "student3" : student3
}

# print(students.items())

# When working with nested dictionaries, .items() allows you to easily unpack both layers.
# Without .items():
# You'd need to manually write something like this:

# for key in students:
#     inner_dict = students[key]
#     for inner_key in inner_dict:
#         print(inner_key, inner_dict[inner_key])

for key, value in students.items():
    # print(key)
    for inner_key, inner_values in value.items():
        # You can use the named parameter end to prevent a newline from printing
        # By default 'end' is a newline, but can be defined as whatever you want (e.g. ", ").
        # https://www.reddit.com/r/learnpython/comments/a1poym/list_of_dictionaries_how_to_print_each_dictkey/
        print(f"{inner_key}: {inner_values},", end=" ")
