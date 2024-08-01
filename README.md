# AeroPass
A local password manager built to generate and manage user passwords for any platform of their choice.

## Usage
Create a .config file in the project folder with a valid Fernet key. You can generate one by executing Fernet.generatekey().decode("utf-8") in another python file. 
Be sure to pip install Fernet and Pyperclip (it will be used later)

As of right now, there is no GUI, as it is still in development. In order to use the script, execute the following in order. You may use either the python file or the terminal to do this.

1. createAccount(username, masterPassword)
This creates a new 'account' which creates a text file formatted as {username.txt} which will store all of your encrypted passwords for each platform. Make sure your master password is something you will remember, as it is what will grant you access to use each function. To confirm that the account creation is successful, you can use validateUser(username, masterpassword)

2. savePassword(username, masterPassword, platform, password)
This function will take the above parameters and store the platform and encrypted password for said platform in a text file named {username.txt}. By default, the password field will be automatically generated using the generatePassword() function, which 
has its own set of parameters listed below:<br/>
  generatePassword(length, numLowers, numCaptials, numDigits, numSpecialCharacters)<br/>
      By default the length=10, numLowers=6, numCaptials=1, numDigits=2, numSpecialCharacters=2. You can change these values as you wish, just be sure that the sum of all characters equals your password length.

3. retrievePassword(username, masterPassword, platform)
Finally, to retrieve a password for a given platform, input your username, masterPassword, and desired platform. The function will search the respective username's file to decrypt and print the plaintext password to the console. It will also copy the password to your clipboard. For this to work, ensure you pip install pyperclip!

