import random
import string
import bcrypt
import os
def generatePassword(length=10, numLowers=6, numCapitals=1, numDigits=2, numSpecialCharacters=1):
    if(type(length) is not int or type(numLowers) is not int or type(numCapitals) is not int or type(numDigits) is not int or type(numSpecialCharacters) is not int):
        raise TypeError("All inputs must be of type int")
    
    if length != numLowers + numCapitals + numDigits + numSpecialCharacters:
        raise ValueError("Desired length must equal total number of desired characters")
    
    
    lowers = random.choices(string.ascii_lowercase, k=numLowers)
    capitals = random.choices(string.ascii_uppercase, k=numCapitals)
    digits = random.choices(string.digits, k=numDigits)
    specialChars = random.choices("^&*!@#$", k=numSpecialCharacters)
    
    combined = lowers + capitals + digits + specialChars 
    random.shuffle(combined)
    
    password =  ''.join(combined)

    return password

def hashPassword(password):
    bytes = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(bytes, bcrypt.gensalt())
    return hashedPassword

def hashAndSavePassword(username, platform, password):
    hashPassword = hashPassword(password)
    platformEntry = platform + ": "
    entry = platformEntry + hashedPassword.decode('utf-8') + "\n"
    f = open(username + ".txt", "a")
    f.write(entry)
    f.close()
    return "Password successfully saved"

def createAccount(username, masterPassword):
    with open("master.txt") as file:
        for line in file:
            if username.lower() in line:
                raise ValueError("Username already exists!")
    f.close()
    hashedPassword = hashPassword(masterPassword)
    usernameEntry = username.lower() + ": "
    entry = usernameEntry + hashedPassword.decode('utf-8') + "\n"
    f = open("master.txt", "a")
    f.write(entry)
    f.close()
    return "Account created: " + username.lower()
    
def signIn(username, masterPassword):
    match = ""
    with open("master.txt") as file:
        for line in file:
            if username.lower() in line:
                match = line
        
    if match != "":
        userTuple = match.strip().split(": ") 
        hashedPw = userTuple[1]
        if bcrypt.checkpw(masterPassword.encode('utf-8'), hashedPw.encode('utf-8')):
            return "Signed in"   
        else:
            raise ValueError("Username or password is incorrect")
    else:
        raise ValueError("Username or password is incorrect")


signIn("Aero", "AeroThunder02")