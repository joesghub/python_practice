#  Write a Python script that takes a user input string and prints the string in reverse order.

# Output Example: 

# Enter a string: hello world
# Reversed string: dlrow olleh

# print("Welcome to Reverse World!")
# print("Here we take whatever string you give to us and reverse it for you!")
import time

print("Welcome to Reverse World!\nHere we take whatever string you give to us and reverse it for you!")

string = input("What would you like reversed today?: ")

# Using f-string for a clean approach
print(f"Lovely! Let's get to reversing \"{string}\"")

reversed_string = string [::-1]

time.sleep(3)

print(f"Ok, we have your reversed statement:\n\"{reversed_string}\"\nThank you for coming to Reverse World!")
