import string
import random

#Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for pasasword from these
        1. Digits
        2. Letters
        3. Special characters
        4. Exit''')
        
characterList = "" #create an empty variable

#Getting chracter set for password
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
        #adding letters to possible characters
        characterList += string.ascii_letters
    elif(choice == 2):
        #adding digits to the password
        characterList += string.digits
    elif(choice == 3):
        #add special characters
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)

print("The random password is " + "".join(password))