# Write a Python script that fetches data from a public API (e.g., a random joke API) and prints the result. 

# Output Example:

# Fetching a joke...
# Here's a joke: Why don't skeletons fight each other? They don't have the guts.

########## VERSION 1: VIEWING RESPONSE ###########

# Print the Raw JSON Response
# Before assuming anything, it's good practice to print the response to see its structure:
# response = requests.get(url)
# print(response.json())  # Print raw JSON output

# import requests
# import json

# def get_word():
#     # Define the API endpoint URL
#     url = 'https://api.dictionaryapi.dev/api/v2/entries/en/service'

#     try:
#         # Make a GET request to the API endpoint using requests.get()
#         response = requests.get(url)
#         word = response.json()
#         print(word)
#     finally:
#         print("Well done!")

# if __name__ == "__main__":
#     get_word()

########## VERSION 2: FORMATTING RESPONSE FOR READABILITY ###########

# import requests
# import json

# def get_word():
#     # Define the API endpoint URL
#     url = 'https://api.dictionaryapi.dev/api/v2/entries/en/cheer'

#     try:
#         # Make a GET request to the API endpoint using requests.get()
#         response = requests.get(url)
#         word = response.json()

#         if isinstance(word, list):  # Check if the response is a list
#             word = word[0]  # Get the first dictionary inside the list

#         print(word.keys())
#         print(json.dumps(word, indent=4))  # Pretty-print JSON
#     finally:
#         print("Well done!")

# if __name__ == "__main__":
#     get_word()

# __name__: This is a built-in Python variable that holds the name of the current module.
# When you run the script directly, __name__ is set to "__main__", so the code inside this block runs.
# When you import the script as a module, __name__ is set to the script’s filename (not "__main__"), so the code inside this block does not run automatically.
# Why Is This Useful?
# It prevents functions from executing when you import the script into another Python file.
# It allows the script to be reused as a module in other programs.

########## VERSION 3: IDEAL FORMATTING BASED ON STRUCTURE EXPLORATION ###########

# https://dictionaryapi.dev/?ref=freepublicapis.com

import requests
import json



def get_word():
    
    choice = input("This application finds all the known definitions for a word you choose!\nWhat word would you like to define?: ")

    # Define the API endpoint URL
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{choice}'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            word = response.json()

            if isinstance(word, list):  # Check if the response is a list
                word = word[0]  # Get the first dictionary inside the list
            print(word.keys())
            
            name = word.get("word")
            print(f"Word: {name}")
            
            for meaning in word.get("meanings"):
                for definition in meaning.get("definitions"):
                    version = definition["definition"]
                    print(f"Definition: {version}")
        else:
            print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors or exceptions
        print(f"Error: Unable to fetch data. {e}")
    

if __name__ == "__main__":
    get_word()




