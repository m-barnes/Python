import docx
import time
import os
from os import system
from pprint import pprint

def check_path(path):
	try:
		os.path.abspath(path)
		os.chdir(path)
	except:
		print('Cannot find that directory. Please wait...')
		time.sleep(2)
		clear()			
		main()	
		
def continue_main():
	continueParse = input('\n\n\nWould you like to parse another file? (y)es or (n)o? ').lower()
	if continueParse == 'y':
		main()
	else: 
		print('Goodbye!')
		time.sleep(2)
		sys.exit()	
	
def clear():
	try: 
		system('cls')
	except:
		system('clear')

def getText(filename):
	print(filename)
	doc = docx.Document(filename)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.text)
	pprint(fullText)
	
def parseFile():				
	try:
		filename = input('\nPlease provide the name of the Word document. ')
		getText(filename + '.docx')
		continue_main()		
	except:
		print('Cannot find that file. Please try again. Please wait...')
		time.sleep(2)
		clear()
		main()

def main():
	print('The current working directory is ', os.getcwd())
	path = input('\nPlease provide the full path to the Word document you wish to parse or press \'enter\' to keep the current directory.\n')
	if len(path)==0:
		path = os.getcwd()	
	else:
		check_path(path)
		
	parseFile()
	
main()

