import os
from PIL import Image

#define some variables. 
SQUARE_FIT_SIZE = 600
#the logo image works best when it's a 32-bit PNG. JPEG and less quality PNG images need converting and other accommodations.
LOGO_FILENAME = 'coltlogo.png'

#open the image and save it as an image object
logoIm = Image.open(LOGO_FILENAME)
#grab the dimensions (it's a tuple) and store them as separate variables. 
logoWidth, logoHeight = logoIm.size


#create a new directory to store the new images with the watermark. 
os.makedirs('withLogo', exist_ok=True)

for filename in os.listdir('.'):
	#if the filename does not end it PNG or JPG ignore it. Also ignore it if it's the logo file.
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == LOGO_FILENAME:
        continue 
	#open the image and convert it to 'RGB' This helps if some of the images in the directory are JPGs. We don't have to deal with transparency masks. 
    im = Image.open(filename).convert('RGB')
    width, height = im.size
	#resize the images. 
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
	#add logo to resized images using paste()
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
	#save the newly logo'ed image. 
    im.save(os.path.join('withLogo', filename))
