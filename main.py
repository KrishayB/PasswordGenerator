# Terminal-based password generator
import string
import random
import os

print("Welcome!")

master = string.ascii_letters + string.digits + string.punctuation
selection = ""
numPassword = 5
passwordLength = 10
containsLetters = 1
containsNumbers = 1
containsPunctuation = 1

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def generatePassword():
    clearTerminal()
    for i in range(numPassword):
        currentPassword = ""
        for j in range(passwordLength):
            if (master != ""):
                currentPassword += random.choice(master)
        print(str(i + 1) + ". " + currentPassword)
    input("Press enter to continue... ")

def configureSettings():
    global master
    clearTerminal()
    print("[1] Number of passwords")
    print("[2] Password length")
    print("[3] Contains Letters")
    print("[4] Contains Numbers")
    print("[5] Contains Punctuation")
    print("[6] Cancel")
    settingsSelection = input("Select an option: ")
    if (settingsSelection == "1"):
        clearTerminal()
        global numPassword
        print("Current number of passwords: " + str(numPassword))
        numPassword = int(input("Set to: "))
        configureSettings()
    elif (settingsSelection == "2"):
        clearTerminal()
        global passwordLength
        print("Current password length: " + str(passwordLength))
        passwordLength = int(input("Set to: "))
        configureSettings()
    elif (settingsSelection == "3"):
        clearTerminal()
        global containsLetters
        print("Whether passwords contain letters: " + str(containsLetters))
        containsLetters = int(input("Set to: "))
        if (containsLetters >= 1):
            master += string.ascii_letters
        elif (containsLetters <= 0):
            master = master.replace(string.ascii_letters, "")
        configureSettings()
    elif (settingsSelection == "4"):
        clearTerminal()
        global containsNumbers
        print("Whether passwords contain numbers: " + str(containsNumbers))
        containsNumbers = int(input("Set to: "))
        if (containsNumbers >= 1):
            master += string.digits
        elif (containsNumbers <= 0):
            master = master.replace(string.digits, "")
        configureSettings()
    elif (settingsSelection == "5"):
        clearTerminal()
        global containsPunctuation
        print("Whether passwords contain punctuation: " + str(containsPunctuation))
        containsPunctuation = int(input("Set to: "))
        if (containsPunctuation >= 1):
            master += string.punctuation
        elif (containsPunctuation <= 0):
            master = master.replace(string.punctuation, "")
        configureSettings()

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