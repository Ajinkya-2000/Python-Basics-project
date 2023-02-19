import random

print("--------------------Password Generator Program-----------------------")

all_chars = ''
# Using Ascii code to get all the possible characters
for i in range(65,91):
    all_chars += chr(i)
for i in range(97,123):
    all_chars += chr(i)
for i in range(0,10):
    all_chars += str(i)
for i in range(33,48):
    all_chars += chr(i)
all_chars += '@'

# all_chars - now contains all the characters we will use for password generation

num = int(input("How many passwords you wish to generate :"))
lenght = int(input("Enter the required length of password :"))

print()
print("Your Password :-")
for i in range(num):
    password = ''
    for i in range(lenght):
        password += random.choice(all_chars)
    print(password)