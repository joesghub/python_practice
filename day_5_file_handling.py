# Write a Python script that reads from a text file named data.txt and prints each line with its line number. 
# Test Script by creating a data.txt file

# Output Example: (data.txt contains:)

# Hello, world!

# Version 1: Works but can be simplified
# file = open("data.txt")
# line = 1
# for x in file:
#     print(f"{line} {x}")
#     line = line +1
# file.close()

# Output:
# 1 Hello World!

# 2 How is it today?

# Version 2: 

# The with statement in Python is used to manage resources like files, sockets, or database connections. 
# It ensures that resources are properly acquired and released, even if errors occur during execution.

# The += operator is a shorthand for incrementing a variable by adding another value to it.
# How it works:
# a += b is equivalent to a = a + b.
# It modifies the value of a by adding the value of b to it and updating a.

# .strip() to remove any trailing newlines or whitespace.

# with open("data.txt") as file:
#     line = 1
#     for x in file:
#         print(f"{line} {x.strip()}")
#         line += 1

# Output:

# 1 Hello, World!
# 2 This is a test.
# 3 Python is fun.

# Version 3:

# The loop works as:
# Extract a tuple from enumerate: Each iteration takes a tuple like (index, value).
# Unpack the tuple: Assigns index to i and value to line.
# Run the body of the loop: In this case, print(f"{i}: {line}").

# The enumerate function wraps the lines list and pairs each item with an index, starting from 1 (because start=1).
# The result of enumerate(lines, start=1) is something like this:
# [(1, "Hello, World!"), (2, "Python is fun."), (3, "Keep learning!")]

with open("data.txt") as file:
    for line, x in enumerate(file, start=1):
        print(f"{line} {x.strip()}")
