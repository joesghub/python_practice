# Write a Python script that takes a number as input and prints whether it is odd or even.

# Output Example:

# Enter a number: 7
# 7 is odd

print("Hello! This application is called \"The Determinator!\"\nWe'll be able to tell you if a number is odd or even.")

number = int(input("Please enter a number to be determined: "))

# print(number)

# print(type(number))

if number % 2 == 0:
    print(f"{number} is even")
else: 
    print(f"{number} is odd")
