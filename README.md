# Password-Manager
This is a simple desktop application which generates random strong passwords and stores on a No-SQL database locally.
It can generate, analyze and save strong password on your system.
## Submodules:
 * User authentication system.
 * Password manager.
 * Password generator.
 * Password strength tester.
## Features:
 ### User Login:
 * User can enter their username and master-password to open the vault.
### Password Manager:
 * A table consiting of stored passwords.
 * Add multiple entries consisting of title, login-id, password, website and any other extra detail.
 * User can update or delete existing entries.
* Passwords can be easily copied to clipboard with a click.

### Password Generator:
User can generate strong random passwords by just setting the length of the password required.
Every password generated contains the following conditions:
* size of password>4 
* one digit 
* one special character
* one uppercase letter
* one lowercase leter

### Password Strength Tester:
User can check the strength of their password and the result is given as :
* very weak
* weak
* strong
* very strong
* unbreakable
## Technologies used:
* python3
* PyQt5
* MongoDB (No-SQL Database)

## Create your own .exe file on your desktop:
 * Must install MongoDB on your system before running the code or creating the .exe file.
 * Then type the following code in the terminal to create the .exe file.
        
          pip install pyinstaller
          pyinstaller main.py                       //for executable with dependencies
          pyinstaller --onefile -w main.py          //standalone executable without terminal
