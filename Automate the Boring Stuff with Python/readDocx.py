import docx
import time
import os
from os import system
from pprint import pprint

finished = False

def getText(filename):
	print(filename)
	doc = docx.Document(filename)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.text)
	pprint(fullText)
	
def clear():
	try: 
		system('cls')
	except:
		system('clear')

while finished == False:
	
	def parseFile():
		print('The current working directory is ', os.getcwd())
		path = input('\nPlease provide the full path to the Word document you wish to parse or press \'enter\' to keep the current directory.\n')
		if len(path)==0:
			path = os.getcwd()	
		try:			
			os.path.abspath(path)
			os.chdir(path)
			
		except:
			print('Cannot find that directory. Please wait...')
			time.sleep(2)
			clear()			
			parseFile()
			
		try:
			filename = input('\nPlease provide the name of the Word document. ')
			getText(filename + '.docx')
			
			continueParse = input('\n\n\nWould you like to parse another file? (y)es or (n)o? ').lower()
			if continueParse == 'y':
				parseFile()
			else: 
				print('Goodbye!')
				time.sleep(2)
				sys.exit()
		except:
			print('Cannot find that file. Please try again. Please wait...')
			time.sleep(2)
			clear()
			parseFile()
		
		
	parseFile()

