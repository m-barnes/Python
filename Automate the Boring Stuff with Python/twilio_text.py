accountSID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+18885555555'
twilioNumber = '+12xxxxxxxxx'

from twilio.rest import Client


def textmyself(text_message):
	twilioCli = Client(accountSID, authToken)
	twilioCli.messages.create(body=text_message, from_= twilioNumber, to = myNumber)
	

