#! python3
#downloadXKCD comics 

import requests, os, bs4, time

url= 'http://xkcd.com'
os.makedirs('G.O.A.T', exist_ok=True)
start_time = time.time()
while not url.endswith('#'):
	#download the page
	print('Downloading page %s...' % url)
	res=requests.get(url)
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
			imageFile = open(os.path.join('G.O.A.T', os.path.basename(comicUrl)), 'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()
			continue
		
		
		
	#get the prev button's url
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')	

end_time = time.time()
elapsed_time = end_time - start_time
minutes = round(elapsed_time//60 % 60)
seconds = round(elapsed_time % 60)
print('All done, yo. Elapsed time: ', minutes, ' minutes and', seconds, 'seconds.')
