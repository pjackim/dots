#This program prompts the user to enter a password using the input function
#The program assigns the input to a variable named passWord
# The len function is used to get the length of the data in the passWord variable
#the len function puts this value in the variable passwordLength
#The length of the passwordLength variable is printed.

#This is the start of the program

username = input("Please enter your username: ")
password = input("Please enter your password: ")

# username length
user_min_length = 5
user_max_length = 10
# password length
pass_min_length = 5
pass_max_length = 10

if len(username) < user_min_length:
    print("Username cannot be shorter than " + str(user_min_length) + " characters.")
elif len(username) > user_max_length:
    print("Username cannot be longer than " + str(user_max_length) + " characters.")
else:
    print("Thank you for following the security policy for user name length")

if len(password) < user_min_length:
    print("Password cannot be shorter than " + str(pass_min_length) + " characters.")
elif len(password) > user_max_length:
    print("Password cannot be longer than " + str(pass_max_length) + " characters.")
else:
    print("Thank you for following the security policy for password name length")
    

# code you gave me
""" 
minLength = 6		#this is the minimum password length
maxLength = 12		#this is the maximum password length
passWord = input("please enter a new password – ")

passwordLength = len(passWord)
if passwordLength < minLength:
    print("your password is " + str(passwordLength) + " characters long")
    print("your password is too short")
    print("your password must be greater than minLength characters")
if passwordLength > maxLength:
    print("your password is " + str(passwordLength) + " characters long")
    print("your password is too long")
    print("your password must be less than maxLength characters")
if (passwordLength > minLength) and (passwordLength < maxLength):
    print("Thank you for creating a strong password!")
"""