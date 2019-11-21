import time
from datetime import datetime


#~ time.time()
#~ def calcProd():
	#~ print("waiting...")
	#~ product  = 1
	#~ for i in range(1, 60000):
		#~ product = product * i 
	#~ return product
	


#~ start_time = time.time()
#~ prod = calcProd()
#~ end_time = time.time()
#~ print('The answer is %s digits long.' % ((len(str(prod)))))
#~ print('This operation took %s seconds to complete.' % (end_time - start_time))

#################################################################################

#time.sleep()


start_time=time.time()
print('Waiting 20 seconds...please hold...')
time.sleep(20)
end_time = time.time()
print('Time elapsed: %s' % (end_time - start_time))





start_time=time.time()
print('Waiting 20 seconds...please hold...')

for i in range(20):
	time.sleep(1)
	
	
end_time = time.time()
print('Time elapsed: %s' % (end_time - start_time))


##################################################################################

#Getting current time



def convert_time(timestamp):
		#take the UTC time passed and convert it to a date/time that we can read. Strip out the hours and minutes. Convert to string.
		UTC_time = datetime.fromtimestamp(timestamp).strftime('%m:%d:%Y %H:%M:%S')
		print(UTC_time)
		#Take the variable above, strip it of everything but the hours and minutes (just in case) and convert from military time. .
		localtime = datetime.strptime(UTC_time, '%m:%d:%Y %H:%M:%S').strftime('%m:%d:%Y %I:%M:%S %p')
		#return the converted time.
		return localtime
		
UTC_time = time.time()
print(UTC_time)


print(convert_time(UTC_time))
