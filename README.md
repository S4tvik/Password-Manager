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
## Output:
  * Login Window
  
    <img src="https://user-images.githubusercontent.com/91609959/226932009-db043289-a3bd-42a7-9175-d437ed220927.png" width="250" >
    
  * Options Window
    
    <img src="https://user-images.githubusercontent.com/91609959/226933770-735bbb47-6900-46f2-be31-3ce5107e004d.png" width="250" >
  
  * Password Generator
    
    <img src="https://user-images.githubusercontent.com/91609959/226933977-f62c37c7-a75d-4e0b-8765-9e413c109255.png" width="250" >
   
  * QR Password
    
    <img src="https://user-images.githubusercontent.com/91609959/226934202-2724ee07-64e7-456f-aedc-656c35fbdec7.png" width="250" >
    
  * Saving Password
    
    <img src="https://user-images.githubusercontent.com/91609959/226934602-45c8e166-a5aa-4bed-9659-f4f2f8aa5e39.png"  >
    
  * Saved Passwords
    
    <img src="https://user-images.githubusercontent.com/91609959/226934934-e40bdbcf-772c-4df3-a7a6-69e88eefea90.png" width="250" >
    
  * Password Strength
    
    <img src="https://user-images.githubusercontent.com/91609959/226935255-522ef0f0-6940-4582-adc5-a7413ffdc1e8.png" width="250" >
    
    <img src="https://user-images.githubusercontent.com/91609959/226935527-f8ec015a-fa0d-4151-a907-eab9d6bc87be.png" width="250" >    <img src="https://user-images.githubusercontent.com/91609959/226935613-56d5ad1b-2483-4245-a0df-49eff62015ea.png" width="250" >    <img src="https://user-images.githubusercontent.com/91609959/226935694-4531a0d1-364a-4420-b92b-a66c819ccee2.png" width="250" >    <img src="https://user-images.githubusercontent.com/91609959/226935773-141dca7e-87a5-44dc-a6e7-ee4a3338a7d2.png" width="250" >    <img src="https://user-images.githubusercontent.com/91609959/226935868-9a1ecf4e-53a4-4635-bde6-cf2f259885fb.png" width="250" >
    
   
   
  

    

