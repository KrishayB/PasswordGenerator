# Terminal-based password generator
import string
import random
import os

print("Welcome!")

selection = ""
numPassword = 5
passwordLength = 10

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def generatePassword():
    clearTerminal()
    for i in range(numPassword):
        currentPassword = ""
        for j in range(passwordLength):
            currentPassword += random.choice(string.ascii_letters)
        print(str(i + 1) + ". " + currentPassword)
    input("Press enter to continue... ")

def configureSettings():
    clearTerminal()
    print("[1] Number of passwords")
    print("[2] Password length")
    print("[3] Cancel")
    settingsSelection = input("Select an option: ")
    if (settingsSelection == "1"):
        clearTerminal()
        global numPassword
        print("Current number of passwords: " + str(numPassword))
        numPassword = int(input("Set to: "))
    elif (settingsSelection == "2"):
        clearTerminal()
        global passwordLength
        print("Current password length: " + str(passwordLength))
        passwordLength = int(input("Set to: "))
    else:
        input("Press enter to continue...")

while (str(selection) != "3"):
    clearTerminal()
    print("[1] Run")
    print("[2] Settings")
    print("[3] Exit")
    selection = input("Select an option: ")

    if (str(selection) == "1"):
        generatePassword()
    elif (str(selection) == "2"):
        configureSettings()

print("\nThanks for using this!")