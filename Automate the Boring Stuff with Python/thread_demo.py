import threading, time

start_time = time.time()
print('Start of Program...')

def nap_time():
	for i in range(1, 90):
		time.sleep(1)
	print('Wake up!')
	end_time = time.time()
	elapsed_time = end_time - start_time
	minutes = round(elapsed_time // 60 % 60)
	seconds = round(elapsed_time % 60)
	print('All done, yo. Elapsed time: ', minutes, ' minutes and', seconds, 'seconds.')

	
threadObj = threading.Thread(target=nap_time)
threadObj.start()

print('End of Program...')


end_time = time.time()
elapsed_time = end_time - start_time
minutes = round(elapsed_time//60 % 60)
seconds = round(elapsed_time % 60)
print('All done, yo. Elapsed time: ', minutes, ' minutes and', seconds, 'seconds.')
	
