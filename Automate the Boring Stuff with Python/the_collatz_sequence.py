#import textwrap to make it pretty
import textwrap

list_of_numbers = []
#def a game function to handle the game stuff
def game():
	print(textwrap.fill('The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.'))	
	#grab some user input, try to parse it, or make them try, try, again.
	try:
		number = int(input('\nPlease enter a number to start: '))
		print('You entered', number)
		list_of_numbers.append(number)
		collatz(number)
	except:
		print('Invalid attempt. Please try again.\n')
		game()
	
#def a function to 'collatz' the number
def collatz(number):
	#check to see if the number is even. If it is, do some math and give some output.
	if number %2 == 0:
		print('\nOkay, since',number, 'is even. So, let\'s divide by 2\n')
		number = number // 2
		list_of_numbers.append(number)
		print(number)
		if number !=1:
			collatz(number)
		else:
			print('\nAnd done! Works every time!\n')
			print('Here\'s the final list. \n', list_of_numbers)
	#check to see if the number is odd. If it is do some math and give some output. 
	elif number%2 == 1:
		print('\nAnd',number, 'is odd. So, let\'s multiply it by 3 and add 1\n')
		number=3*number+1
		list_of_numbers.append(number)
		print(number)
		collatz(number)

#call the game function	
game()
	
	
	


