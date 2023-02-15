'''
import random
def play(name):
    ch = {1:'r',2:'p',3:'s'}
    user_count,comp_count = 0,0

    while user_count!=3 and comp_count!=3:
        comp = random.choice(['r','p','s'])   # r-rock,p-paper,s-scissors
        user = int(input("Enter your choice 1.Rock 2.Paper 3.Scissors :"))
        if comp == ch[user]:
            print("Its a Tie!")
        elif comp == 'r' and ch[user] == 's':
            print(f"Computer - {comp} x {ch[user]} - User")
            comp_count += 1
            print(f"Computer {comp_count} User {user_count}")
        elif comp == 'r' and ch[user] == 'p':
            print(f"Computer - {comp} x {ch[user]} - User")
            user_count += 1
            print(f"Computer {comp_count} User {user_count}")
        elif comp == 'p' and ch[user] == 'r':
            print(f"Computer - {comp} x {ch[user]} - User")
            comp_count += 1
            print(f"Computer {comp_count} User {user_count}")
        elif comp == 'p' and ch[user] == 's':
            print(f"Computer - {comp} x {ch[user]} - User")
            user_count += 1
            print(f"Computer {comp_count} User {user_count}")
        elif comp == 's' and ch[user] == 'r':
            print(f"Computer - {comp} x {ch[user]} - User")
            user_count += 1
            print(f"Computer {comp_count} User {user_count}")
        else:
            print(f"Computer - {comp} x {ch[user]} - User")
            comp_count += 1
            print(f"Computer {comp_count} User {user_count}")
    
    if user_count == 3:
        print(f"Congratulations! {name} you won")
    else:
        print(f"Mr.Computer Won")

# Calling the function
print("Let play !!!!!\nRock Paper Scissors\nIt's a best of 5 game")
play('Ajinkya')
'''


# Other way 
import random
def play(name):
    ch = {1:'Rock',2:'Paper',3:'Scissor'}
    user_count,comp_count = 0,0

    while user_count!=3 and comp_count!=3:

        comp = random.choice(['Rock','Paper','Scissor'])   
        user = int(input("Enter your choice 1.Rock 2.Paper 3.Scissors :"))
        if comp == ch[user]:
            print("Its a Tie!")
            print(f"Both selected {comp}")
        elif comp == 'Rock' and ch[user] == 'Scissor' or comp == 'Paper' and ch[user] == 'Rock'   or  comp == 'Scissor' and ch[user] == 'paper':
             print(f"Computer - {comp} x {ch[user]} - User")
             comp_count += 1
             print(f"Computer {comp_count} User {user_count}")
        else:
            print(f"Computer - {comp} x {ch[user]} - User")
            user_count += 1
            print(f"Computer {comp_count} User {user_count}")

    if user_count == 3:
        print()
        print(f"Congratulations! {name} you won!!!!")
    else:
        print()
        print(f"Mr.Computer Won")


print("----------------------Rock Paper Scissor Game--------------------------")
name = input("Enter your name to play :")
print(f"Player who wins 3 points wins the match\nAll the Best {name}!")
play(name)