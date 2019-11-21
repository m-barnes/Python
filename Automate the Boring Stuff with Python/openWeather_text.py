import json, sys, time, requests
from datetime import datetime
from datetime import date
import calendar

import smtplib
from email.mime.text import MIMEText

from twilio_text import textmyself



#defined function to convert time. It's a thing.
def convert_time(timestamp):
		#grab the UTC time and grab just the hours and minutes.
		UTC_time = datetime.fromtimestamp(timestamp).strftime('%H:%M')
		#convert UTC time to local time and in standard format.
		localtime = datetime.strptime(UTC_time, '%H:%M').strftime('%I:%M %p')
		#return the converted time.
		return localtime

#defined function to query the API and print output.
def get_weather(location):
	#Secret API key. Sssshhhh! Don't tell anyone.
	appID = 'xxxxxxxxxxxxxxxxxxxxxxx'
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
	weatherData = page.json()
	# check the data type
	# ~ print(type(weatherData))
	#if the data returned is no good, provide an error message and kill the application.
	if weatherData['cod'] == '404':
		print('That is not a valid zip code. Please try again.')
	
	#grab the day of the week.
	day_week = date.today()
	#store the formatted data into a variable and format it using the format() . JSON Object -> Python Dictionary (example data returned is below). Convert the time, round float numbers, and add suffix signs.
	weather_text = '''\
	
	Current weather for: {location}
	{date} {time}
	Condition: {condition}
	Temperature: {temp} deg. F
	Humidity: {humidity} %
	Sunrise: {sunrise}
	Sunset: {sunset}
	\
	'''.format(location = weatherData['name'], date = calendar.day_name[day_week.weekday()], time = convert_time(weatherData['dt']), condition = weatherData['weather'][0]['description'].title(), temp = round(int(weatherData['main']['temp'])), humidity = round(int(weatherData['main']['humidity'])), sunrise = convert_time(weatherData['sys']['sunrise']), sunset = convert_time(weatherData['sys']['sunset']))
	return(weather_text)
	
def send_text(text_message):
	msg = MIMEText(text_message)
	msg['Subject'] = 'The current weather forecast'
	msg = msg.as_string()
	
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login('m.brandon.barnes@gmail.com', 'xxxxxxxxxxxxxxx')
	smtpObj.sendmail('weather-bot', '8885555555@txt.att.net', msg)
	smtpObj.quit()
	

try:	
	#grab the zipcode from the arguments passed	
	location = ' '.join(sys.argv[1:])
	text_message = get_weather(location)
	textmyself(text_message)
	send_text(text_message)
	
	
except:
	if len(sys.argv) < 2:
		print('Please enter a zip code')
		



#returned JSON data from API
	#{'coord': {'lon': -92.38, 'lat': 36.33}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 281.59, 'pressure': 1019, 'humidity': 93, 'temp_min': 279.82, 'temp_max': 284.26}, 'visibility': 16093, 'wind': {'speed': 2.1}, 'rain': {}, 'clouds': {'all': 90}, 'dt': 1572387413, 'sys': {'type': 1, 'id': 3492, 'country': 'US', 'sunrise': 1572352160, 'sunset': 1572391018}, 'timezone': -18000, 'id': 0, 'name': 'Mountain Home', 'cod': 200}
 
