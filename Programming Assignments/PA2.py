# Elinnoel Nunez
# Program #2: The Trig Calculator
# COSC 1306
# Spring 2021
# Calculates sin, cos, tan of an angle given in degree into radians

from math import pi     # You cannot use any of the modules provided by Python

# Define the factorial function here
def factorial(num):
    if num < 1:
        return 1
    else:
        return num * factorial(num-1)

# Define the sin function
def sin(num, terms):
    value = num

    for n in range(1, terms):
        constant = (-1) ** n
        numerator = num ** ((2*n) + 1)
        denominator = factorial((2*n) + 1)
        cur = (numerator / denominator) * constant
        value+= cur    
    return value

# Define the cos function
def cos(num, terms):
    value = 1

    for n in range(1, terms):
        constant = (-1) ** n
        numerator = num ** (2*n)
        denominator = factorial(2*n)
        cur = (numerator / denominator) * constant
        value+= cur    
    return value

def degTorad(value):
    return value * pi / 180

def printMenu():
    print("THE TRIGONOMETRIC CALCULATOR") 
    print("1 - Calculate the sine of a value")
    print("2 - Calculate the cosine of a value")
    print("3 - Calculate the tangent of a value")
    print("4 - Exit")

option = 0
while option != 4: # Use a loop here
    printMenu() # Call the printMenu function here
    option = int(input("Enter your option: "))
    if option == 1 or option == 2 or option == 3:# Write the condition here
        value = int(input("Enter the value (in degrees): "))
        terms = int(input("Enter the number of terms: "))
        radians = degTorad(value) # Call the degTorad function here
        if option == 1:# Write the condition here
            result = sin(radians,terms)# Call the sin function here
            print("The sine of",value,"is %.4f" %result)
        elif option == 2:# Write the condition here
            result = cos(radians, terms)# Call the cos function here
            print("The cosine of",value,"is %.4f" %result) 
        elif option == 3:# Write the condition here
            if value == 90 or value == 270:
                print("The tangent of",value,"is undefined")
            else:
                result = sin(radians, terms) / cos(radians, terms) # Use the sin and cos functions to calculate the tangent
                print("The tangent of",value,"is %.4f" %result)
    elif option != 4: # Write the condition here
        print("Invalid Option. Please try again")
    else:
        break
