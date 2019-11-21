import os

import census2010

done = False
banner_art = ''' _____                                _____  _____  __   _____  
/  __ \                              / __  \|  _  |/  | |  _  | 
| /  \/  ___  _ __   ___  _   _  ___ `' / /'| |/' |`| | | |/' | 
| |     / _ \| '_ \ / __|| | | |/ __|  / /  |  /| | | | |  /| | 
| \__/\|  __/| | | |\__ \| |_| |\__ \./ /___\ |_/ /_| |_\ |_/ / 
 \____/ \___||_| |_||___/ \__,_||___/\_____/ \___/ \___/ \___/ '''
 
logo = '''
  |* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
  | * * * * * * * * *  :::::::::::::::::::::::::|
  |* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
  | * * * * * * * * *  :::::::::::::::::::::::::|
  |* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
  | * * * * * * * * *  ::::::::::::::::::::;::::|
  |* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
  |:::::::::::::::::::::::::::::::::::::::::::::|
  |OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
  |:::::::::::::::::::::::::::::::::::::::::::::|
  |OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
  |:::::::::::::::::::::::::::::::::::::::::::::|
  |OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|
'''

print(banner_art)
print(logo)

while done == False:
	try:
		state = input('\n\n\nPlease enter the two letter postal abbreviation for the state: ').upper()
		county = input('\nPlease enter the full name of the county: ').title()

		county_pop = census2010.allData[state][county]['pop']

		print('\n\n\nThe population of',county, 'county in', state,'in 2010 was' +(format(county_pop, ' ,d')), '\n\n\n')
		
		census_done = input('Would you like to make a different selection? (y)es or (n)o: ')
		print('\n\n\n')
		
		if census_done == 'y':
			done = False
		else:
			print('\n\n\nThank you for using Census2010! Have a great day!')
			done = True
	except: 
		print('\n\nYou entered:\nState: ',state,'\nCounty: ', county)
		print('\n\nWe cannot find that state and/or county in our census data. Check your spelling and try again.\n\n\n')
