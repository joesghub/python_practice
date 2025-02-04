# Write a script that monitors the size of a specific directory 
# and sends an alert (print a message) if it exceeds a certain size limit.

# Output Example:

# Monitoring directory size...
# Directory size: 75 MB
# Monitoring directory size...
# Directory size: 120 MB
# Alert: Directory size exceeded the limit of 100 MB!

###### VERSION 1 #########

# path to folder
# loop through files in folder
# getsize of each file
# add file size to folder size
# print folder size


# using getsize function os.path module
# import os


# try: 
#     abs_path =input("Path: ")
#     print("Monitoring directory size...")
#     folder_size = 0
#     for file in abs_path:
#     for file in abs_path: iterates over each character in the input string, not the files in the directory.
#         file_size = os.path.getsize(file)
#         folder_size =+ file_size
#         This mistakenly assigns +file_size (a positive number) to folder_size instead of adding to it.
#     if folder_size < 100:
#         print("Directory size: ", file_size, "MB")
# except FileNotFoundError:
#     print(f"Error: The file '{abs_path}' was not found. Please check the file path or name.")
# else:
#     print("Alert: Directory size exceeded the limit of 100 MB!")




###### VERSION 2 #########

# path to folder
# loop through files in folder
# check if file or directory
# getsize of each file
# add file size to folder size
# print folder size


# import os

# try: 
#     abs_path =input("Path: ")
#     if not os.path.isdir(abs_path):
#         print("Error: The provided path is not a directory.")
#         exit()
#     print("Monitoring directory size...")
#     path_files = os.listdir(abs_path)
#     # print(path_files)
#     folder_size = 0
#     for file in path_files:
#         file = os.path.join(abs_path, file)
#         # print(file)
#         if os.path.isfile(file):
#             file_size = os.path.getsize(file)
#             print(file_size)
#             folder_size += file_size
#             print(folder_size)
#     final_folder_size = round(folder_size / (1024 * 1024), 2)
#     if final_folder_size < 100:
#         print("Directory size: ", final_folder_size, "MB")
#     else:
#         print("Alert: Directory size exceeded the limit of 100 MB!")
# except FileNotFoundError:
#     print(f"Error: The directory '{abs_path}' was not found. Please check the path name.")


########### VERSION 3 ###########
import os
import time

# Set directory size limit in MB
SIZE_LIMIT_MB = 100

try:
    abs_path = input("Enter directory path: ")

    # Validate that the path is a directory
    if not os.path.isdir(abs_path):
        print("Error: The provided path is not a directory.")
        exit()

    print("Monitoring directory size... Press Ctrl+C to stop.\n")

    while True:  # Continuous monitoring loop
        folder_size = 0  # Reset size each loop

        # Get the total size of all files in the directory
        for file in os.listdir(abs_path):
            file_path = os.path.join(abs_path, file)
            if os.path.isfile(file_path):
                folder_size += os.path.getsize(file_path)

        # Convert size to MB
        final_folder_size = round(folder_size / (1024 * 1024), 2)

        # Print the directory size
        print(f"Directory size: {final_folder_size} MB")

        # Check if size exceeds limit
        if final_folder_size > SIZE_LIMIT_MB:
            print(f"⚠️ Alert: Directory size exceeded the limit of {SIZE_LIMIT_MB} MB!\n")

        # Wait for a few seconds before checking again
        time.sleep(5)  # Adjust interval as needed

except FileNotFoundError:
    print(f"Error: The directory '{abs_path}' was not found. Please check the path name.")
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
