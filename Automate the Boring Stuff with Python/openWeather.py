import json, sys, time, requests
from datetime import datetime
from datetime import date
import calendar

#defined function to convert time. It's a thing.
def convert_time(timestamp):
		#take the UTC time passed and convert it to a date/time that we can read. Strip out the hours and minutes.
		UTC_time = datetime.fromtimestamp(timestamp).strftime('%H:%M')
		#Take the variable above, strip it of everything but the hours and minutes (just in case) and convert from military time. .
		localtime = datetime.strptime(UTC_time, '%H:%M').strftime('%I:%M %p')
		#return the converted time.
		return localtime

#defined function to query the API and print output.
def get_weather(location):
	#Secret API key. Sssshhhh! Don't tell anyone.
	appID = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
	#form the query URL using the location zip code and API key.
	url ='https://api.openweathermap.org/data/2.5/weather?zip=%s,us&units=imperial&appid=%s' % (location, appID)
	page = ''
	#while page is empty, query the API for data. 
	while page == '':
		try:
			page = requests.get(url)
			break
		except:
			print("Connection refused by the server. Please wait...")
			time.sleep(5)
			print("Trying connection again. Please wait...")
			continue
			
	# Load JSON data into a Python variable (dictionary).
	
	# ~ print(page.json())
	weatherData = page.json()
	# check the data type
	# ~ print(type(weatherData))
	print(weatherData['weather'])
	#if the data returned is no good, provide an error message and kill the application.
	if weatherData['cod'] == '404':
		print('That is not a valid zip code. Please try again.')
	
	#grab the day of the week.
	day_week = date.today()
	#print the formatted data. JSON Object -> Python Dictionary (example data returned is below). Convert the time, round float numbers, and add suffix signs.
	print(
	'\nCurrent weather for:\n\n' + weatherData['name'] + '\n' + calendar.day_name[day_week.weekday()], convert_time(weatherData['dt']),
	'\n\nCondition:\t\t', weatherData['weather'][0]['description'].title(),
	'\nTemperature:\t\t',round(int(weatherData['main']['temp'])),chr(176),
	'\nHumidity:\t\t',round(int(weatherData['main']['humidity'])),'%',
	'\nSunrise:\t\t', convert_time(weatherData['sys']['sunrise']),
	'\nSunset:\t\t\t',convert_time(weatherData['sys']['sunset'])
	)

try:	
	#grab the zipcode from the arguments passed	
	location = ' '.join(sys.argv[1:])
	get_weather(location)	
	
except:
	if len(sys.argv) < 2:
		print('Please enter a zip code')
		
		

	

#returned JSON data from API
	#{'coord': {'lon': -92.38, 'lat': 36.33}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 281.59, 'pressure': 1019, 'humidity': 93, 'temp_min': 279.82, 'temp_max': 284.26}, 'visibility': 16093, 'wind': {'speed': 2.1}, 'rain': {}, 'clouds': {'all': 90}, 'dt': 1572387413, 'sys': {'type': 1, 'id': 3492, 'country': 'US', 'sunrise': 1572352160, 'sunset': 1572391018}, 'timezone': -18000, 'id': 0, 'name': 'Mountain Home', 'cod': 200}
 
