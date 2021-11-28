"""  Elinnoel Nunez
     Program #4: The Phonebook program
     COSC 1306
     Spring 2021
"""

# Write the user defined functions here.
def readFromFile(filename):
    list = []
    f = open(f"{filename}", "r")

    fileData = f.readlines()
    for line in fileData:
        list.append(line.split())
    f.close()
    return list

# def readFromFile(filename):
#     list1 = []

#     file1 = open(filename,"r")

#     while True:
#         line = file1.readline()
#         if not line:
#             break
#         else:
#             list1.append(line.split())

#     file1.close()

#     return list1

# print(readFromFile("string.txt"))

def printMenu():
    print("1. Print Contact List")
    print("2. Add New Contact")
    print("3. Delete Contact")
    print("4. Modify Contact")
    print("5. Exit")

def printContactList(list):
    for idx in range(len(list)):
        print(f"Contact # {idx+1}")
        print(f" First name: {list[idx][0]}, Last name: {list[idx][1]}, Phone number: {list[idx][2]}, Birthday: {list[idx][3]}")

def addContact(list):
    fname = input("Enter the First Name: ")
    lname = input("Enter the Last Name: ")
    phone = int(input("Enter the Phone Number: "))
    bday = input("Enter the Birthday: ")
    newContactList = [fname, lname, phone, bday]
    list.append(newContactList)

def deleteContact(list):
    deleteIdx = int(input("Select the contact to be deleted: "))
    if 0 >= deleteIdx or deleteIdx > len(list):
        print("Incorrect contact number")
    else:
        del list[deleteIdx-1]
        print(f"Contact {deleteIdx} deleted")

def modifyContact(list):
    modifyIdx = int(input("Select the contact to be changed: "))
    if 0 >= modifyIdx or modifyIdx > len(list):
        print("Incorrect contact number")
    else:
        fname = input("Enter the First Name: ")
        lname = input("Enter the Last Name: ")
        phone = int(input("Enter the Phone Number: "))
        bday = input("Enter the Birthday: ")
        modifiedList = [fname, lname, phone, bday]
        list[modifyIdx-1] = modifiedList
        print(f"Contact {modifyIdx} was changed")

filename = input("Enter the file name: ")
contactList = readFromFile(filename)

menuOption = 0
while menuOption != 5:
    printMenu()
    menuOption = int(input("Enter your option: "))
    if menuOption == 1:
        printContactList(contactList)
    elif menuOption == 2:
        addContact(contactList)
    elif menuOption == 3:
        deleteContact(contactList)
    elif menuOption == 4:
        modifyContact(contactList)
    elif menuOption != 5:
        print("Invalid option")

