import requests, os, bs4, threading, time

os.makedirs('MultiThread', exist_ok=True)
start_time = time.time()

def downloadXkcd(startComic, endComic):	
	url= 'http://xkcd.com'
	for urlNumber in range(startComic, endComic):		
		#download the page
		print('Downloading page %s...' % urlNumber)
		res = requests.get('http://xkcd.com/%s' % (urlNumber))
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text, features="html.parser")

		#find the URL of the comic page
		comicElem = soup.select('#comic img')
		if comicElem == []:
			print('Could not find comic image.')
		else:
			try:
				comicUrl = 'http' + comicElem[0].get('src')
				#download the image
				print('Downloading image %s...' % (comicUrl))
				res = requests.get(comicUrl)
				res.raise_for_status()
			except requests.exceptions.MissingSchema:
				#skip the comic
				prevLink = soup.select('a[rel="prev"]')[0]
				url = 'http://xkcd.com' + prevLink.get('href')
				#save the image to the folder
				imageFile = open(os.path.join('MultiThread', os.path.basename(comicUrl)), 'wb')
				for chunk in res.iter_content(100000):
					imageFile.write(chunk)
					imageFile.close()
				continue
	
		

downloadThreads = [] 
for i in range(1, 1400, 100): 
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()


for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
	
	
end_time = time.time()
elapsed_time = end_time - start_time
minutes = round(elapsed_time//60 % 60)
seconds = round(elapsed_time % 60)
print('All Finished, Boss. Elapsed time: ', minutes, ' minutes and', seconds, 'seconds.')
