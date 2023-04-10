
# Guess the number
import random
import pyttsx3

# Using pyttsx3 for voice assistance in the game
machine = pyttsx3.init() 

def Guess_Number(x):
    
    # Getting a random number to guess
    random_num = random.randint(1,x)
    guess = 0

    n = input("Enter your name to play :-")

    # The loop where user will guess the number - along with speak assistance
    while guess != random_num:
        guess = int(input(f"Guess the number between 1 to {x} :"))

        if guess < random_num:
            print("Sorry! Your guess is low")
            machine.say("Sorry! Your guess is low")
            machine.runAndWait()

        elif guess > random_num:
            print("Sorry! Your guess is high")
            machine.say("Sorry! Your guess is high")
            machine.runAndWait()
    
    print(f"Congratulation! {n}\nYou guessed the number {random_num}")
    machine.say(f"Congratulation! {n}\nYou guessed the number {random_num}")
    machine.runAndWait()


# Calling the function - Guessing Game
print("----------------------------------Guess The Number --------------------------------------")
Guess_Number(20)
print()



# Computer Guessing the number

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
    print(f"Hooray!\nComputer guessed the number {guess}")
    machine.say(f"Hooray!\nComputer guessed the number {guess}")
    machine.runAndWait()


n = 100
print("--------------------------------Computer Guess The Number -----------------------------------")
a = int(input(f"Enter the number between 1 to {n} that the computer should guess :"))
Computer_GuessNumber(n)
    