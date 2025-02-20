# ### **Practice Problems**  

import os 
import re # 2

############# 1. **Basic Math Operations**: Write a program to calculate the factorial of a number.  

# - number
# - multiply
# - print product

##### Factorial Loop Version ########

# num = input("Enter the number you'd like to find the Factorial of: ")

# if not num.isdigit():
#     print("Error: The provided value is not an integer.")
#     exit()

# factorial = 1
# for i in range(int(num)):
#     # print(f"range index: {i}")
#     fixed = int(i) + 1
#     # print(f"fixed is index + 1: {fixed}")
#     factorial = fixed * factorial
#     # print(f"factorial: is {fixed} * {factorial}")
# print(factorial)


###### Factorial Recursive Version #########

# def factorial(n):
#     if n == 0:  # Base case: factorial of 0 or 1 is 1
#         return 1
#     return n * factorial(n - 1)  # Recursive case

# num = input("Enter a number: ")

# if not num.isdigit() or int(num) < 0:
#     print("Error: Please enter a valid positive integer.")
# else:
#     print(f"Factorial of {num} is {factorial(int(num))}")


################ 2. **String Parsing**: Reverse a string and check if it’s a palindrome.  ###################

# - take string input 
# - parse letters into a list
# - check reverse order
# - compare orders for matching
# - if they match it is a palindrome


######## VERSION 1 String Parsing #########

# check = input("What string would you like to check for palindromeness: ")
# Strings are already iterable, so there’s no need to convert them into a list.
# list(check) and check[::-1] behave the same way, so it's extra work.

# if isinstance(check, str):
#     list_check = list(check)
#     # print(list_check)
#     reversed = list_check[::-1]
#     # print(reversed)
# Strings are already iterable, so there’s no need to convert them into a list.
# list(check) and check[::-1] behave the same way, so it's extra work.
#     if list_check == reversed:
#         print(f"Your string \"{check}\" is a palindrome!")
#     else:
#         print(f"Your string \"{check}\" is not a palindrome.")

########## VERSION 2 String Parsing #########

# check = input("What string would you like to check for palindromeness: ")
# # "Racecar" (capital R) would not be recognized as a palindrome.
# # "A man a plan a canal Panama" wouldn’t work due to spaces.
# # We clean the input to ensure our function works as intended. 
# cleaned_check = check.replace(" ", "").lower()
# reversed_check = check[::-1]
# if cleaned_check == reversed_check:
#     print(f"Your string \"{check}\" is a palindrome!")
# else:
#     print(f"Your string \"{check}\" is not a palindrome.")


########## FINAL Recursion String Parsing #########


# def palindrome(s):
#     # Clean the string: remove spaces and convert to lowercase
#     clean_s = s.replace(" ", "").lower()

#     # Base case: If the string is empty or 1 character, it's a palindrome
#     if len(clean_s) <= 1:
#         return True
    
#     # Recursive case: Check first and last character, then the inner substring
#     if clean_s[0] == clean_s[-1]:
#         return palindrome(clean_s[1:-1])  # Recursive call with the inner string
    
#     return False  # If characters don't match, it's not a palindrome


# # Get user input
# check = input("What string would you like to check for palindromeness: ")

# # Run the recursive function and print the result
# if palindrome(check):
#     print(f"Your string \"{check}\" is a palindrome!")
# else:
#     print(f"Your string \"{check}\" is not a palindrome.")

################# 3. **List Manipulation**: Remove duplicates from a list while maintaining order.  ###################



 ######## V1 List Manipulation #######
# def dedupe(l):
#     # Read first and second word in the list
#     first = l[0]
    
    
#     # Base case: If there is only one items or less in the list, it has no duplicates
#     if len(l) <= 1:
#         return True
#     # Recursive: compare the word against the rest in the list, if it matches a word remove the word from the list 
#     for item in l:
#         if first == item:
#             item.pop()
#             return dedupe(l)
        
# dupes = input("List of duplicates: ")

# # Run the recursive function and print the result
# if dedupe(dupes):
#     print(f"Your list \"{dupes}\" is deduplicated")
# else:
#     print(f"Your list \"{dupes}\" did not have duplicates")

######## V2 List Manipulation #############

# def dedupe(l):
#     # Create an empty list to store unique elements
#     unique_list = []
    
#     # Iterate through the original list
#     for item in l:
#         # Check if item is already in unique_list
#         if item not in unique_list:
#             unique_list.append(item)
    
#     return unique_list
        
# dupes = list(input("List of duplicates: "))

# # Run the recursive function and print the result
# if dedupe(dupes):
#     print(f"Your list is deduplicated.  \"{}\"  ")
# else:
#     print(f"Your list \"{dupes}\" did not have duplicates.")


######## V3 List Manipulation #############

# def dedupe(l):
#     # Create an empty list to store unique elements
#     unique_list = []
    
#     # Iterate through the original list
#     for item in l:
#         # Check if item is already in unique_list
#         if item not in unique_list:
#             unique_list.append(item)
    
#     return unique_list
        
# # Use .split() to properly handle space-separated input.
# # This ensures "1 2 2 3" is read as ["1", "2", "2", "3"] instead of ["1", " ", "2", " ", "2", " ", "3"].
# dupes = input("List of duplicates (separate with spaces): ").split()

# # Run the recursive function and print the result
# if dedupe(dupes):
#     # Capture the return value in a variable and use it in the print statement.
#     result = dedupe(dupes)  
#     print(f"Your list is deduplicated: {result}")
# else:
#     print(f"Your list \"{dupes}\" did not have duplicates.")


# ######## V4 List Manipulation #############

# def dedupe(l):
#     # Create an empty list to store unique elements
#     unique_list = []

#     first = l[0]
    
#     # Base case: If there is only one items or less in the list, it has no duplicates
#     if len(l) <= 1:
#         return True

#     # Check if item is already in unique_list
#     if first not in unique_list:
#         unique_list.append(first)
    
#     return dedupe[1:]
        
# # Use .split() to properly handle space-separated input.
# # This ensures "1 2 2 3" is read as ["1", "2", "2", "3"] instead of ["1", " ", "2", " ", "2", " ", "3"].
# dupes = input("List of duplicates (separate with spaces): ").split()

# # Run the recursive function and print the result
# if dedupe(dupes):
#     # Capture the return value in a variable and use it in the print statement.
#     result = dedupe(dupes)  
#     print(f"Your list is deduplicated: {result}")
# else:
#     print(f"Your list \"{dupes}\" did not have duplicates.")


# ######## V5 List Manipulation #############

# def dedupe(l, unique_list=None):
#     if unique_list is None:
#         unique_list = []

#     first = l[0]
    
#     # Base case: If there is only one items or less in the list, it has no duplicates
#     if len(l) == 0:
#         return l

#     # Check if item is already in unique_list
#     if first not in unique_list:
#         unique_list.append(first)
#     return dedupe(l[1:], unique_list)
        
# # Use .split() to properly handle space-separated input.
# # This ensures "1 2 2 3" is read as ["1", "2", "2", "3"] instead of ["1", " ", "2", " ", "2", " ", "3"].
# dupes = input("List of duplicates (separate with spaces): ").split()

# # Run the recursive function and print the result
# result = dedupe(dupes)  
# print(f"Your list is deduplicated: {result}")


######### FINAL List Manipulation ##########

# def dedupe(l, unique_list=None):
#     # Initialize unique_list only in the first function call (prevents resetting on each recursive call)
#     if unique_list is None:
#         unique_list = []

#     # Base Case: When list is empty, return the accumulated unique_list (stopping condition)
#     if len(l) == 0:
#         return unique_list  # ⬅️ FIXED: Returns the correct list of unique elements

#     # Process the first element
#     first = l[0]

#     # If it's not in unique_list, add it
#     if first not in unique_list:
#         unique_list.append(first)

#     # Recursive Step: Call dedupe() on the remaining elements of l (excluding the first element)
#     return dedupe(l[1:], unique_list)

# # Get user input, splitting it into a list of words/numbers
# dupes = input("List of duplicates (separate with spaces): ").split()

# # Call the function and print the result
# result = dedupe(dupes)  
# print(f"Your list is deduplicated: {result}")



#################### 4. **Dictionary Operations**: Count the occurrences of each word in a given string.  ###################


########### V1 Word Counter ##############

# def word_counter(str):
#   string = input("What passage would you like to have Word Counted?: ").split()

#   word_count = {}

#   for word in string:
#     if string.count(word) > 1:
#       # Instead of word_count.append(word:string.count(word)), use dictionary assignment
#       word_count[word] = string.count(word)
#     else:
#       word_count.append(word:1)
  
#   print(f"Your final word count is: {word_count} ")

# Function Parameters:

# The function should take str as an argument instead of asking for input inside the function.
# The input() call should be outside the function, and you should pass the input string to word_counter().
# Incorrect Use of append() on Dictionary:

# .append() is used for lists, not dictionaries.
# Instead of word_count.append(word:string.count(word)), use dictionary assignment:
# python
# Copy
# Edit
# word_count[word] = string.count(word)
# Inefficiency in count() Calls:

# string.count(word) runs through the entire list for every word, making the function O(n²) (quadratic time complexity).
# Instead, iterate through the words once and update the dictionary incrementally.


########### V2 Word Counter ##############

# def word_counter(str):

#   word_count = {}

#   for word in str:
#     if str.count(word) > 1:
#       word_count[word] = ("{word}:str.count(word)")
#     else:
#       word_count[word] = ("{word}:1")
# print(f"Your final word count is: {word_count} ")

# string = input("What passage would you like to have Word Counted?: ").split()

# word_counter(string)

# Key Issues & Fixes
# Fix word_count.append()

# Issue: Dictionaries don’t have .append(), that's for lists.
# Fix: Use word_count[word] = 1 instead.
# Remove Inefficient string.count(word)

# Issue: string.count(word) recalculates occurrences for each word, making it O(n²).
# Fix: Instead, iterate through string once and increment counts as you go.
# Function Parameter Naming Conflict

# Issue: You're naming the function parameter str, which overrides Python’s built-in str type.
# Fix: Rename it to text or words.
# Fix Input Handling

# Issue: Right now, input() is inside the function.
# Fix: Move input() outside the function and pass string.split() as an argument.



########### V3 Word Counter ##############

# def word_counter(words):

#   word_count = {}
  
#   for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# print(f"Your final word count is: {word_count} ")

# word_counter(words)

# words = input("What passage would you like to have Word Counted?: ").split()

# Key Fixes
# Move Input Before Function Call

# Issue: word_counter(words) runs before words is defined.
# Fix: Move words = input(...).split() above the function call.
# Print Statement Placement

# Issue: print(f"Your final word count is: {word_count} ") is outside the function.
# Fix: Move it inside the function.
# Actually Call word_counter(words)

# Issue: You defined words after calling word_counter(words), so words is undefined.
# Fix: Call word_counter(words) after defining words.


########### V4 Word Counter ##############

# def word_counter(words):

#   word_count = {}
  
#   for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
    
#   print(f"Your final word count is: {word_count} ")

# words = input("What passage would you like to have Word Counted?: ").split()

# word_counter(words)

# Now that your function works, can you format the output to look nicer?
# 🔹 Instead of { 'word': count }, try printing each word & count on a new line.

########### FINAL Word Counter ##############

# def word_counter(words):

#   word_count = {}
  
#   for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
    
#   for word, count in word_count.items():
#     print(f"{word}: {count}")

#   print("\n".join(f"{word}: {count}" for word, count in word_count.items()))
#     This works because:
#     f"{word}: {count}" formats each word-count pair.
#     "\n".join(...) joins them into a multi-line string.


# words = input("What passage would you like to have Word Counted?: ").split()

# word_counter(words)



#################### 5. **Loops**: Generate the Fibonacci sequence up to `n`.  ###################


########### V1 Fibonacci ##############
# def fibonacci(n):

#     count = int(n)

#     a = 0

#     b = 1

#     while count > 0:
#         temp = a  # Store old a
#         print(f"Old A is: {temp}")
#         a = b      # Update a to the old b
#         print(f"B was: {b}")
#         print(f"A is now: {a}")
#         b = temp + b  # Update b
#         print(f"Old A + Old B is: {b}")
#         count -= 1
#         print(f"Count is: {count}")
#     print(f"Final Sum: {b}")

# This is the key part of the Fibonacci logic.

# What it does:
# Updates a to the value of b (the current Fibonacci number).
# Updates b to the sum of the old a and b, which gives the next Fibonacci number.
# How the updates happen:
# This line:
# a, b = b, a + b
# is equivalent to:
# temp = a  # Store old a
# a = b     # Update a to old b
# b = temp + b  # Update b to the sum of old a and b
# But tuple unpacking allows us to do this in a single line.


# number = input("What number?: ")


# fibonacci(number)

# While Loop vs. For Loop:

# Your approach uses a while loop to iterate until count becomes zero. While this works, a for loop is more natural when you know the number of iterations (like n-1 in this case).
# The intended solution uses a for loop because the number of Fibonacci numbers we need to generate is known upfront.
# Printing vs. Storing:

# In your approach, you print the Fibonacci numbers as they're generated. This is useful for debugging, but when you want to return a list of numbers, it’s better to store them in a list.
# The intended solution stores the Fibonacci numbers in a list (sequence) and returns the entire sequence at the end.
# Tuple Unpacking:

# Your approach manually updates a and b, using a temporary variable temp for swapping. The intended solution uses Python’s tuple unpacking (a, b = b, a + b), which is more concise and avoids the need for a temporary variable.


########### FINAL Fibonacci ##############
# def fibonacci(n):
#     n = int(n)  # Ensure input is an integer
#     a, b = 0, 1
#     sequence = [a]  # Start with the first Fibonacci number
    
#     for _ in range(n - 1):  # Generate the next `n-1` numbers
#         sequence.append(b)   # Add the next Fibonacci number
#         a, b = b, a + b      # Update values using tuple swap

#     return sequence  # Return the list of Fibonacci numbers

# # Get user input and call function
# number = input("What number?: ")
# result = fibonacci(number)
# print(f"Fibonacci sequence up to {number}: {result}")

# 1. for _ in range(n - 1):
# This is a for loop that runs n - 1 times.
# _ is a throwaway variable, meaning we don’t actually use it inside the loop. It's just there because Python requires a loop variable.
# range(n - 1) means:
# If n = 5, range(n - 1) → range(4), so the loop runs 4 times.
# Why n - 1?
# We already start the sequence with the first Fibonacci number (0).
# The loop runs to generate the remaining n-1 Fibonacci numbers.
