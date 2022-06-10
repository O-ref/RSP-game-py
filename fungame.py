#fun game
from random import choice

done = False

all_choices = ["rock", "paper", "scissors"]
computer_score = 0
user_score = 0


#loop game
while not done:
	choice_made = None
	#generate random move from computer
	computer_choice = choice(all_choices)
	#User enter moves
	user_input = input("\nEnter R for Rock, P for Paper or S for Scissors. Enter x to quit: ")
	#validate user's input
	if user_input == 'R':
		user_choice == 'rock'
		choice_made = "valid"
	elif user_input == 'P':
		user_choice == 'paper'
		choice_made = "valid"
	elif user_input == 'S':
		user_choice == 'scissors'
		choice_made = "valid"
	elif user_input == 'x':
			choice_made = "quit"
	else:
		print("invalid input. try again!")
		
		#if user input is valid, compare
		if choice_made == "valid":
			print(f"computer select\'{computer_choice}\', user select \'{user_choice}\' ")
		
		
		#if user input is to quit, end program
		if choice_made == "quit":
			print("Thanks for playing")
			print(f"Final score: computer = {computer_score}, user = {user_score}")
		
		