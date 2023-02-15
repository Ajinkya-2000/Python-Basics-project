
# Guess the number
import random
def Guess_Number(x):
    random_num = random.randint(1,x)
    guess = 0

    while guess != random_num:
        guess = int(input(f"Guess the number between 1 to {x} :"))
        if guess < random_num:
            print("Sorry! Your guess is low")
        elif guess > random_num:
            print("Sorry! Your guess is high")
    
    print(f"Congratulation!\nYou guessed the number {random_num}")

# Calling the function - Giving range for the number
print("---------------------Guess The Number ----------------------")
Guess_Number(10)
print()



# Computer Guessing the number
import random
def Computer_GuessNumber(n):
    msg = ''
    l,h = 1,n
    while msg != 'c':
        if l != h:
            guess = random.randint(l,h)
        else:
            guess = l
        msg = input(f"If {guess} Low(l) or High(h) or Correct(c) :")
        if msg == 'l':
            l = guess + 1
        elif msg == 'h':
            h = guess - 1
    print(f"Congralutions!\nComputer guessed the number {guess}")


n = 100
print("---------------------Computer Guess The Number ----------------------")
a = int(input(f"Enter the number between 1 to {n} that the computer should guess :"))
Computer_GuessNumber(n)
    