import random
import string
from cryptography.fernet import Fernet
import os

with open('.config', 'r') as file:
    KEY = file.readline().strip()

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

def createAccount(username, masterPassword):
    filename = username.lower() + ".txt"
    try:
        with open(filename, 'x') as file:
            pass
    except FileExistsError:
        print(f"The account '{username.lower()}' already exists.")
    
    hashedPassword = encryptPassword(masterPassword)
    usernameEntry = username.lower() + ": "
    entry = usernameEntry + hashedPassword.decode('utf-8') + "\n"
    f = open("master.txt", "a")
    f.write(entry)
    f.close()
    return "Account created: " + username.lower()

def validatePassword(encryptedPw, providedPw, key):
    fernet = Fernet(key)
    decryptedPw = fernet.decrypt(encryptedPw)
    return decryptedPw.decode('utf-8') == providedPw    

def validateUser(username, masterPassword):
    match = ""
    with open("master.txt") as file:
        for line in file:
            if username.lower() in line:
                match = line
        
    if match != "":
        userTuple = match.strip().split(": ") 
        encryptedPw = userTuple[1]

        if validatePassword(encryptedPw, masterPassword, KEY):
            return "User validated"   
        else:
            raise ValueError("Username or master password is incorrect")
    else:
        raise ValueError("Username or master password is incorrect")



def decryptPassword(encryptedPw):
    fernet = Fernet(KEY)
    return fernet.decrypt(encryptedPw)    

def encryptPassword(password):
    cipherSuite = Fernet(KEY)
    cipherText = cipherSuite.encrypt(password.encode("utf-8"))
    return cipherText

def savePassword(username, masterPassword, platform, password=generatePassword()):
    validateUser(username, masterPassword)
    with open(username.lower() + ".txt") as file:
        for line in file:
            if platform.lower() in line:
                raise ValueError("Platform already exists!")
    bytes = encryptPassword(password)
    platformEntry = platform.lower() + ": "
    entry = platformEntry + bytes.decode('utf-8') + "\n"
    f = open(username + ".txt", "a")
    f.write(entry)
    f.close()
    return f"Password for '{platform.lower()}' successfully generated"

def retrievePassword(username, masterPassword, platform):
    validateUser(username, masterPassword)
    filename = username.lower() + ".txt"
    if os.path.isfile(filename):
        match = ""
        with open(filename) as file:
            for line in file:
                if platform.lower() in line:
                    match = line
            
        if match != "":
            platformTuple = match.strip().split(": ") 
            encryptedPw = platformTuple[1]
            return f"Your password for '{platform}' is '{decryptPassword(encryptedPw).decode('utf-8')}'"

        else:
            raise ValueError("No password associated with given platform")

    else:
        raise ValueError("No account associated with username, please create an account to proceed")


print(retrievePassword("aero", "AeroThunder02", "Steam"))