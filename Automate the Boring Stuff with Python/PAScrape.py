#! python3
#download Penny Arcade comics 

import requests, os, bs4

url= 'https://www.penny-arcade.com/comic'
os.makedirs('G.O.A.T', exist_ok=True)

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
			comicUrl = comicElem[0].get('src')
			#download the image
			print('Downloading image %s...' % (comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			#skip the comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'https://www.penny-arcade.com/comic' + prevLink.get('href')
			continue
		
		#save the image to the folder
		
		imageFile = open(os.path.join('G.O.A.T', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		
	#get the prev button's url
	prevLink = soup.select('a[title="Previous"]')[0]
	url =  prevLink.get('href')	













print('Done')
