import time, subprocess

import pyaudio
import wave

#~ def playsong():
	#~ filename = 'countdown.wav'

	#~ # Set chunk size of 1024 samples per data frame
	#~ chunk = 1024  

	#~ # Open the sound file 
	#~ wf = wave.open(filename, 'rb')

	#~ # Create an interface to PortAudio
	#~ p = pyaudio.PyAudio()

	#~ # Open a .Stream object to write the WAV file to
	#~ # 'output = True' indicates that the sound will be played rather than recorded
	#~ stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
					#~ channels = wf.getnchannels(),
					#~ rate = wf.getframerate(),
					#~ output = True)

	#~ # Read data in chunks
	#~ data = wf.readframes(chunk)

	#~ # Play the sound by writing the audio data to the stream
	#~ while data != '':
		#~ stream.write(data)
		#~ data = wf.readframes(chunk)

	#~ # Close and terminate the stream
	#~ stream.close()
	#~ p.terminate()

def countdown(timeleft):	
	while timeleft != 0:
		if timeleft == 1:
			print(timeleft)
			print('get ready!')
			subprocess.Popen(['start', 'countdown.wav'], shell=True)
			#~ playsong()
		else:			
			print(timeleft, ' ')
			time.sleep(1)
		timeleft -= 1
	
	

timeleft = int(input('Please enter a starting value (in seconds): '))




countdown(timeleft)
