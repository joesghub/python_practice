# Write a Python function fahrenheit_to_celsius(fahrenheit) that converts a temperature from Fahrenheit to Celsius. 
# The script should prompt the user for a temperature in Fahrenheit, use the function to convert it and print the result.

# Output Example: 

# Enter temperature in Fahrenheit: 98.6
# 98.6 Fahrenheit is 37.0 Celsius

def fahrenheit_to_celsius():
    fahrenheit = float(input("Please enter a temperature in Farenheit: "))
    celcius = (fahrenheit - 32) * (5/9)
    print(f"{fahrenheit} Fahrenheit is {celcius} Celcius")

fahrenheit_to_celsius()
