# Elinnoel Nunez
# Program #1: The Area Calculator
# COSC 1306
# Spring 2021
# Calculates area based on shape chosen from list. (square, rectange, triangle)

print("Select a figure from the menu:")
print("1 - Square")
print("2 - Rectangle")
print("3 - Triangle")
selection = int(input("Enter your selection: "))

if selection == 1:
    base = int(input("Enter the side length: "))
    area = base ** 2
    print("The area of the selected figure is: %.2f" % (area))
elif selection == 2:
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    print("The area of the selected figure is: %.2f" % (length * width))
elif selection == 3:
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = (base * height) / 2
    print("The area of the selected figure is %.2f" % (area))
else:
    print("Invalid option")