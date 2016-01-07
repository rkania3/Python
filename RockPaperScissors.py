#Python Rock-Paper-Scissors Game
import time
from random import randint


def	play_game():
	playing = True
	wins = 0
	loses = 0
	ties = 0
	print "Let\'s play Rock, Paper, Scissors!"
	while playing:
		you = get_input()
		comp = computer_play()
		if you == 'quit':
			print "Goodbye!"
			playing = False
		else:
			if you == comp:
				print r"It's a tie!"
				ties = ties + 1
			elif (you == 'rock' and comp == 'paper') or (you == 'paper' and comp == 'scissors') or (you == 'scissors' and comp == 'rock'):
				print "The Computer played " + comp + ". You lose!"
				loses = loses + 1
			elif (you == 'paper' and comp == 'rock') or (you == 'scissors' and comp == 'paper') or (you == 'rock' and comp == 'scissors'):
				print "The Computer played " + comp + ". You win!"
				wins = wins + 1	
		print "You: " + str(wins) + " Computer: " + str(loses) + " Ties: " + str(ties)
		
def	get_input():
	option = input(r"Ready? Type 1 for Rock, 2 for Paper, or 3 for Scissors! Or type 0 to quit ")
	if option == 1:
		return 'rock'
	elif option == 2:
		return 'paper'
	elif option == 3:
		return 'scissors'
	else:
		return 'quit'
	
def	computer_play():
	option = randint(1,3)
	if option == 1:
		return 'rock'
	elif option == 2:
		return 'paper'
	else:
		return 'scissors'		
		
play_game()

