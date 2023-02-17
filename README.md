Python Basic projects

1. Guess the Number [user guess and Computer guess]
i) User Guess 
	a. In the first part, user has to guess a number between a given range.
	   The game is active until the user guesses the correct number.
	   The computer helps user by giving hints(too low,too high, correct)
	b. I have used library 'random' for selecting a random number between that range.
	   The exact functionality is 'randint(range_of_numbers)'
ii) Computer Guess
	a. In this part, computer tries to guess a number that user has selected.
	   The game is active until the computer guesses the correct number.
	   User guides the computer by giving hints(l-low guess,h-high guess,c-correct guess)
	b. I have used library 'random' for the selection of a random number by the computer.
	   The concept of binary search is used to guess the number.
	   
2. Rock Paper Scissor
i) This is a Computer vs Player game. The one who wins 3 points wins the game.
ii) Random library is used so that computer can select one option out of the three(rock,paper,scissor)
    [random.choice() used]
iii) For user, I have created a input where the user can select rock paper or scissor by typing 1,2,3
	 [1.Rock 2.Paper 3.Scissor]