# Modify the script from Day 5 to include error handling for file not found errors and print an appropriate message if the file does not exist.

# Output Example:

# Error: The file 'data.txt' was not found. Please check the file path or name.

###### VERSION 1 #######

# print("This application is called Make a Script.\nWith our app you can make any text file a script!")

# path = input("Please enter the absolute path to your text file: ")

# try:
#     with open(path) as file:
# If the file is large, file.read() loads everything at once, which is inefficient.
#         print(file.read())
# except Exception as e:
# Instead of Exception as e, it's better to catch FileNotFoundError specifically.
#     print(f"Error: The file '{path}' was not found. Please check the file path or name | {e}")
# else:
# You open the file twice: once in the try block and again in the else block.
# The second with open(path) inside else is unnecessary and inefficient.
#     with open(path) as exists:
#         for line, x in enumerate(exists, start=1):
#                 print(f"{line} {x.strip()}")
# finally:
#      print(f"Your file \"{path}\" is a script now!")

###### VERSION 2 #######

print("This application is called Make a Script.\nWith our app you can make any text file a script!")

path = input("Please enter the absolute path to your text file: ")

try:
    with open(path) as file:
        content = file.readlines()  # Read all lines once
except FileNotFoundError:
    print(f"Error: The file '{path}' was not found. Please check the file path or name.")
else:
    print("\nYour file contents as a script:\n")
    for line, x in enumerate(content, start=1):
        print(f"{line} {x.strip()}")
    print(f"\nYour file \"{path}\" is now a script!")
