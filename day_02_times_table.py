# Create a list of the first 10 numbers and write a script that prints each number multiplied by 2.

# Output Example: 

# 0 * 2 = 0
# 1 * 2 = 2
# 2 * 2 = 4
# 3 * 2 = 6
# 4 * 2 = 8
# 5 * 2 = 10
# 6 * 2 = 12
# 7 * 2 = 14
# 8 * 2 = 16
# 9 * 2 = 18

mylist = list(range(10))

print(mylist)

for i in mylist:
    multiplied = i * 2
    print(f"{i} * 2 = {multiplied}")
