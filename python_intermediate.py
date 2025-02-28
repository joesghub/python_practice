# ## **Stage 2: Intermediate Concepts (Weeks 3–4)**  
# Learn how to apply Python in more complex scenarios and use standard libraries.  

# ### **Topics to Learn**  
# - File handling (read, write, and parse files)  
# - Error handling (try-except)  
# - Regular expressions  
# - Functions: lambda, map, filter, reduce  
# - Basic data structures (stacks, queues)  

# ### **Practice Problems**  
# 1. **File Parsing**: Write a script to parse a log file and extract error messages.  
# 2. **Regex**: Extract email addresses from a block of text.  
# 3. **Data Structures**: Implement a queue using a list.  
# 4. **Error Handling**: Create a robust script to divide two numbers, handling division by zero.  
# 5. **Map/Filter**: Given a list of numbers, filter out all the even numbers and square the rest.  


####################### 1. **File Parsing**: Write a script to parse a log file and extract error messages. #######################

# Here are some guiding questions to help you think through the problem:
# How will you open and read a file in Python?
# How will you go through each line to check for errors?
# What keyword or pattern will indicate an error in the log?
# How will you store and display the extracted errors?
# Your first task:
# Write a simple script to open and print each line of the file.
# Once you do that, try to identify lines that contain "ERROR" and only print those.

# 1. open file 
# 2. read file 
# 3. set matching phrase(s)
# 4. capture entire log message (set ending punctuation)
# 5. store multiple messages
# 6. print them out for review 

############ V1 Error Checker ############

# def error_checker():

#     path = input("Please enter the absolute path to your log file: ")

#     with open(path) as file:
#         content = file.readlines() # Returns a list of lines from the file
#         # ['[INFO] Server started successfully.\n', '[ERROR] Failed to connect to database.\n', '[WARNING] High memory usage detected.\n', '[INFO] User logged in.\n', '[ERROR] Timeout while connecting to API.\n', '[DEBUG] Cache cleared successfully.\n', '[INFO] Scheduled job executed.\n', '[ERROR] Unable to read configuration file.\n', '[WARNING] Disk space running low.\n', '[INFO] Server shutting down.\n']
        
#         # content = file.read() # Returns the file content
#         # [INFO] Server started successfully.
#         # [ERROR] Failed to connect to database.
#         # [WARNING] High memory usage detected.
#         # [INFO] User logged in.
#         # [ERROR] Timeout while connecting to API.
#         # [DEBUG] Cache cleared successfully.
#         # [INFO] Scheduled job executed.
#         # [ERROR] Unable to read configuration file.
#         # [WARNING] Disk space running low.
#         # [INFO] Server shutting down.


#     print(content)

# error_checker()

############ V2 Error Checker ############

# def error_checker():

#     path = input("Please enter the absolute path to your log file: ")

#     with open(path) as file:
#         content = file.readlines() # Returns a list of lines from the file

#         errors = []

#         for i in content:
#             if 'ERROR' in i:
#                 errors.append(i)


#     print(errors)

# error_checker()

# ['[ERROR] Failed to connect to database.\n', '[ERROR] Timeout while connecting to API.\n', '[ERROR] Unable to read configuration file.\n']

############ V3 Error Checker ############

# def error_checker():

#     # Takes path to file as input
#     path = input("Please enter the absolute path to your log file: ")

#     errors = []
#     # Initialize errors = [] before the try block to avoid issues if an exception occurs.

#     # Error handling block using try and except
#     try:
#         # With Open, opens and closes file without using .close()
#         with open(path) as file:
#             content = file.readlines() # Returns a list of lines from the file

#             errors = [line.strip() for line in content if "ERROR" in line] # Applies .strip to each line in the log file that contains "ERROR" and saves it to a list.
#         # Prints the compiled list of errors
#         print(errors)
#         # Move the print(errors) inside the try block so it only runs when no exception is raised.

#     # Error message if file is not found error occurs
#     except FileNotFoundError:
#         print(f"Error: The file '{path}' was not found. Please check the file path or name.")
#      # Error message if permission error occurs
#     except PermissionError:
#         print(f"Error: You do not have the permissions to access the file '{path}'. Please update the permissions and try again.")
        

# error_checker()

############ FINAL Error Checker ############

# def error_checker():
#     """
#     Reads a log file and extracts lines containing 'ERROR'.
#     Handles file access errors gracefully.
#     """
#     path = input("Please enter the absolute path to your log file: ")

#     errors = []  # Ensure errors is always defined

#     try:
#         with open(path) as file:
#             errors = [line.strip() for line in file if "ERROR" in line]  # List comprehension

#         print("Errors found in log file:")
#         for error in errors:
#             print(error)

#     except FileNotFoundError:
#         print(f"Error: The file '{path}' was not found. Please check the file path or name.")
#     except PermissionError:
#         print(f"Error: You do not have permission to access the file '{path}'. Please update the permissions and try again.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# error_checker()


####################### 2. **Regex**: Extract email addresses from a block of text. #######################

import re

############ V1 Email Extractor ############

# def email_extractor():

#     text_file = input("What is the absolute path to your file?: ")

#     emails = []

#     try:
#         with open(text_file) as file:
#             emails = [line.strip() for line in file if re.findall(".*@.*[.].*", file)]
#             # You're applying re.findall to file, but file is a file object, not the text content. You need to apply it to line instead.
#             # Instead of filtering lines, use re.findall(pattern, line) and extend your emails list with the matches.
#             # Your current regex (".*@.*[.].*") is too broad and will match anything with an @ and a .
#         print(f"These are the emails extracted from your text file: ")
#         for email in emails:
#             print(email)

#     except FileNotFoundError:
#         print(f"Error: The file '{text_file}' was not found. Please check the file path or name.")
#     except PermissionError:
#         print(f"Error: You do not have permission to access the file '{text_file}'. Please update the permissions and try again.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# email_extractor()

# r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# [a-zA-Z0-9._%+-]+

# [a-zA-Z0-9._%+-] → Matches any of the following characters:
# Lowercase (a-z)
# Uppercase (A-Z)
# Digits (0-9)
# Special characters (_ . % + -) (which are commonly allowed in email usernames)
# + → Means one or more occurrences of these characters.
# @

# Matches the @ symbol literally (since all valid emails must have this).
# [a-zA-Z0-9.-]+

# [a-zA-Z0-9.-] → Matches:
# Lowercase (a-z)
# Uppercase (A-Z)
# Digits (0-9)
# Special characters (.-) (commonly found in domain names, e.g., sub.domain.com)
# + → Again, one or more of these characters.
# \.

# The \. is an escaped period (.) because a regular dot (.) in regex means "any character".
# Since domain names always contain a literal period (e.g., .com or .org), we must escape it with \. to match an actual dot.
# [a-zA-Z]{2,}

# [a-zA-Z] → Matches only letters (uppercase or lowercase).
# {2,} → Means at least 2 letters.
# This ensures that we correctly match domains like .com, .org, .edu, .co.uk, etc., while avoiding single-letter top-level domains, which don't exist.


############ FINAL Email Extractor ############

# def email_extractor():

#     text_file = input("What is the absolute path to your file?: ")

#     emails = []

#     try:
#         with open(text_file, "r") as file:
#             content = file.read() # Read the entire file as a string
#             emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)
#         if emails:
#             print(f"There are {len(emails)} emails in your text file.")
#             print("These are the emails extracted from your text file:")
#             for email in emails:
#                 print(email)
#         else:
#             print("No emails were found in the file.")

            
#     except FileNotFoundError:
#         print(f"Error: The file '{text_file}' was not found. Please check the file path or name.")
#     except PermissionError:
#         print(f"Error: You do not have permission to access the file '{text_file}'. Please update the permissions and try again.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# email_extractor()


# RESULTS
# What is the absolute path to your file?: emails.txt
# There are 7 emails in your text file.
# These are the emails extracted from your text file:
# support@example.com
# billing@finance-company.org
# manager@company-email.com
# noreply@system.net
# hello-world@domain.co.uk
# John.Doe@Gmail.com
# Stacy.QuiNN@Gmail.com.ask

####################### 3. **Data Structures**: Implement a queue using a list.  #######################

############ V1 LIst Queue ############

# queue = []  # Initialize an empty queue

# # Function to add an item to the queue
# def enqueue(item):
#     queue.append(item)
#     print(f"Enqueued: {item}")

# # Function to remove an item from the queue
# def dequeue():
#     if queue:
#         item = queue.pop(0)  # Remove the first item (FIFO)
#         print(f"Dequeued: {item}")
#         return item
#     else:
#         print("Queue is empty!")
#         return None

# # Test the queue
# enqueue("A")
# enqueue("B")
# enqueue("C")

# dequeue()
# dequeue()
# dequeue()
# dequeue()  # This should print "Queue is empty!"

# 1. Why can't I write this all as one function?
# Technically, you can write everything in one function, but it would make the code less flexible and harder to maintain. Here's why we separate enqueue and dequeue:

# Separation of concerns:
# enqueue(item): Only adds items to the queue.
# dequeue(): Only removes items from the queue.
# If you put both operations in one function, you’d need a way to decide whether to add or remove, which makes it more complex.
# Modularity:
# Having separate functions allows you to use enqueue and dequeue independently.
# In real applications, you might want to enqueue items in one place and dequeue them somewhere else.


# 2. Why do we use if queue: for popping but not for appending?
# Yes, if queue: checks whether the list is empty. Here’s why it's needed:
# Appending (enqueue) never fails:
# queue.append(item) always works, even if the queue is empty.
# No need to check anything beforehand.
# Popping (dequeue) can fail:
# queue.pop(0) removes the first item, but if the queue is empty, Python raises an IndexError.
# if queue: prevents this error by checking if there's anything to remove.
# The else clause prints "Queue is empty!" instead of crashing the program.

# 3. Experiment with User Input (Optional)
# If you want to interact with the queue, modify the script to take user input:

# while True:
#     action = input("Enter 'enqueue' to add, 'dequeue' to remove, or 'exit' to quit: ").strip().lower()
    
#     if action == 'enqueue':
#         item = input("Enter an item to add: ")
#         enqueue(item)
#         display_queue()
#     elif action == 'dequeue':
#         print("Dequeued:", dequeue())
#         display_queue()
#     elif action == 'exit':
#         print("Exiting...")
#         break
#     else:
#         print("Invalid command. Try again.")


############ V2 LIst Queue ############

# class Queue:

#     def __init__(self,queue):
#         self.queue = []
#         pass
# You're taking queue as a parameter, but you never use it.
# You should initialize self.queue as an empty list without any parameters (unless you plan to start with a pre-filled queue).

#     def enqueue(a):
#         print(f"Adding {a} to the queue...")
#         self.queue.append(a)
#         print(f"Enqueued: {a}")
#         pass
# Instance methods must have self as the first parameter to access instance attributes (self.queue).
# Methods like enqueue() and dequeue() don't have self, so Python doesn't know which object's queue you're modifying.

#     def dequeue():
#         if self.queue:
#             a = self.queue.pop(0)
#             print(f"Dequeued: {a}")
#         else:
#             print("Queue is empty!")
#         pass

#     def display_queue():
#         print(f"The current queue is: {self.queue}")

# ✅ What You Need to Fix:
# Ensure all instance methods include self as the first parameter.
# Fix __init__() to properly initialize self.queue.
# Use self.queue.append(a) and self.queue.pop(0) correctly within methods.


############ FINAL LIst Queue ############

# class Queue:

#     def __init__(self):
#         self.queue = []
#         pass

#     def enqueue(self, a):
#         print(f"Adding {a} to the queue...")
#         self.queue.append(a)
#         print(f"Enqueued: {a}")
#         pass

#     def dequeue(self):
#         if self.queue:
#             item = self.queue.pop(0)
#             print(f"Dequeued: {item}")
#         else:
#             print("Queue is empty!")
#         pass

#     def display_queue(self):
#         print(f"The current queue is: {self.queue}")

# # Testing

# q = Queue()
# q.enqueue("Task 1")
# q.enqueue("Task 2")
# q.display_queue()
# q.dequeue()
# q.display_queue()
# q.dequeue()
# q.dequeue()  # Test empty queue case

# # Results

# Adding Task 1 to the queue...
# Enqueued: Task 1
# Adding Task 2 to the queue...
# Enqueued: Task 2
# The current queue is: ['Task 1', 'Task 2']
# Dequeued: Task 1
# The current queue is: ['Task 2']
# Dequeued: Task 2
# Queue is empty!


# 🛠️ Possible Refinements:
# Remove Unnecessary pass Statements

# pass is only needed if a function is empty. Since all methods have actual code, you can remove pass.
# Improve display_queue() for Clarity

# If the queue is empty, you might want a special message instead of printing an empty list.

####################### 4. **Error Handling**: Create a robust script to divide two numbers, handling division by zero.   #######################


############ V1 Simple Divsion ############

# def simple_division():

#     try:
#         if isdigit(num1) and isdigit(num2):
#             a = int(num1)
#             b = int(num2)
#         result = a / b 
#         print(f"The quotient of {a} and {b} is: {result}")
#     except ZeroDivisionError:
#         print(f"Sorry, you can not divide by zero. Please choose two new numbers.")
#         simple_division()
#     except ValueError:
#         print(f"Sorry, you have not entered numerical digits. Please choose two numbers you would like to divide.")
#         simple_division()
#     except Exception as e:
#         print(f"Sorry, you have run into an error. {e}. Please choose two numbers you would like to divide.")
#         simple_division()

#     # Intro
#     print("Let's divide two numbers!")

#     num1 = input("What is the first number you would like to divide?: ")

#     num2 = input("What is the second number you would like to divide?: ")

# simple_division()

# 🔴 Issues to Fix
# Variables (num1 & num2) Are Used Before They're Defined

# You are checking isdigit(num1) and isdigit(num2) before the user even enters them.
# Move the user input section to the beginning of the function.
# isdigit() Is Not Called on Strings Properly

# isdigit() is a method of strings, so you need to use it like this: num1.isdigit().
# This only works for positive integers, not decimals or negative numbers.
# Use try-except to catch invalid inputs instead of isdigit().
# Recursion (simple_division()) Is Not Always Ideal

# If the user enters bad input repeatedly, this could cause a stack overflow.
# Instead of calling the function again, consider using a loop to ask for new input.
    
# 🛠 Your Next Steps
# 🔹 Move the user input section to the beginning of the function.
# 🔹 Use try-except instead of isdigit() for validation.
# 🔹 Replace recursion with a loop to keep asking for input if there's an error.
    

############ FINAL Simple Divsion ############

# def simple_division():

#     # Intro
#     print("Let's divide two numbers!")

#     while True: # Keep looping until we get valid input
#         try:
#             num1 = float(input("What is the first number you would like to divide?: "))
#             num2 = float(input(f"What number would you like to divide {num1} by?: "))

#             result = num1 / num2 
#             print(f"The quotient of {num1} and {num2} is: {result}")
#             break # Exit loop if division is successful

#         except ZeroDivisionError:
#             print(f"Sorry, you can not divide by zero. Please choose two new numbers.")
#         except ValueError:
#             print(f"Sorry, you have not entered numerical digits. Please choose two numbers you would like to divide.")
#         except Exception as e:
#             print(f"Sorry, you have run into an error. {e}. Please choose two numbers you would like to divide.")


# simple_division()


####################### 5. **Map/Filter**: Given a list of numbers, filter out all the even numbers and square the rest. #######################

############ V1 Filter and Square ############

# def square_odds():
#     odds = []

#     squares = []

#     nums = input("Please enter a list of numbers: ")

#     for d in nums:
#         odds = filter(d % 2 == 1, nums)

#     for d in odds:
#         squares = map(d ** 2, odds)

#     print(f"The filtered and squared results of your list {nums} is: ")
#     for d in squares:
#         print(d)

# 🔹 Guided Fixes
# Convert nums from a string into a list of integers.
# Use lambda functions or list comprehensions with filter() and map().
# Ensure you're storing the results properly before printing them.

############ V2 Filter and Square ############

# def square_odds():
#     odds = []

#     squares = []

#     nums = input("Please enter a list of numbers: ").split()

#     is_odd = lambda x: if x % 2 = 1 return True else return False
#     # lambda functions don’t use if statements explicitly.

#     power_up = lambda x: x ** 2

#     filtered = filter(is_odd, nums)

#     for d in filtered:
#         odds.append(d)
    
#     squared = map(power_up, odds)

#     for d in squared:
#         squared.append(d)

#     print(f"The filtered and squared results of your list {nums} is: ")
#     for d in squares:
#         print(d)

# 🔹 Next Steps
# Try fixing these issues one at a time:

# Fix the lambda syntax.
# Convert nums to integers.
# Convert filter() and map() results to lists.
# Store squared numbers correctly.


############ V3 Filter and Square ############

# def square_odds():
#     odds = []

#     squares = []

#     nums = [int(x) for x in input("Enter a list of numbers: ").split()]
#     # .split() → Breaks input into separate numbers.
#     # int(x) for x in ... → Converts each string to an integer.

#     is_odd = lambda x: x % 2 == 1
#     # This automatically returns True if x is odd and False otherwise.

#     power_up = lambda x: x ** 2

#     filtered = filter(is_odd, nums)

#     for d in filtered:
#         odds.append(d)
    
#     squared = map(power_up, odds)

#     for d in squared:
#         squares.append(d)

#     print(f"The filtered and squared results of your list {nums} is: ")
#     for d in squares:
#         print(d)

#     ✅ Yes, it works, but it's inefficient because you're manually storing intermediate values when filter() and map() already return the needed results.


############ V4 Filter and Square ############

# def square_odds():
#     nums = [int(x) for x in input("Enter a list of numbers: ").split()]

#     is_odd = lambda x: x % 2 == 1
#     power_up = lambda x: x ** 2

#     filtered = filter(is_odd, nums)
#     squared = map(power_up, filtered)  # Use `filtered` directly, no need for `odds`

#     print(f"The filtered and squared results of your list {nums} is: ")
#     for d in squared:  # Directly loop over `squared`, no need for extra storage
#         print(d)

############ FINAL Filter and Square ############

# def square_odds():
#     nums = [int(x) for x in input("Enter a list of numbers: ").split()]

#     square_and_filter = [x ** 2 for x in nums if x % 2 == 1]
#     # x for x in nums → Loops through each number in nums
#     # if x % 2 == 1 → Only keeps the odd numbers

#     print(f"The filtered and squared results of your list {nums} is: ")
#     for d in square_and_filter:  
#         print(d)

# square_odds()

# 🔥 Now that’s Pythonic! 🔥

# Look at how concise and clean it is! You replaced multiple lines of filter() and map() with one elegant list comprehension.

# Why is this better?
# ✅ Faster Execution – List comprehensions are optimized in Python’s internal implementation.
# ✅ Easier to Read – The logic is all in one place, making it more intuitive.
# ✅ Less Code, Same Power – No need for extra loops or .append() calls.

# You nailed it! 🚀 Want to try making this even more flexible? (Hint: Maybe let the user choose whether to square even or odd numbers? 😏)
