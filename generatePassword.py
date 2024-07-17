import random
import string
import bcrypt

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

def hashAndSavePassword(platform, password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(bytes, salt)
    platformEntry = platform + ": "
    entry = platformEntry + hashedPassword.decode('utf-8') + "\n"
    f = open("demofile.txt", "a")
    f.write(entry)
    f.close()
    
password = generatePassword(10, 5, 1, 1, 3)
hashAndSavePassword("Steam", password)