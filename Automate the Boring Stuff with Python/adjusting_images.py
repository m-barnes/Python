from PIL import Image
import os


#open an image and get some info
mario = Image.open('mario.png')

print(mario.size)

width, height = mario.size
print(width)
print(height)

print(mario.filename)
print(mario.format_description)

print('*' * 100)

#create a new image (200 x 200 color: red)
new_image = Image.new('RGBA', (200, 200), 'red')
new_image.save('red.png')
print('Image created at', os.getcwd())

print('*' * 100)

#crop an existing image

cropped_mario = mario.crop((302, 239, 891, 851))
print('Image cropped successfully')
cropped_mario.save('mario_cropped.png')
print('Image saved')

print('*' * 100)

#resize an existing image. 

quartersized = mario.resize((int(width / 2), int(height / 2)))
quartersized.save('tiny_mario.png')
print('Image resized')

print('*' * 100)

#rotating images.
mario.rotate(90).save('mario_90.png')
print('Image rotated 90 degrees')
mario.rotate(180).save('mario_180.png')
print('Image rotated 180 degrees')

mario.rotate(6).save('mario_6.png')
mario.rotate(6, expand=True).save('mario_6_expanded.png')
print('Image rotated 6 degrees and expanded')

mario.transpose(Image.FLIP_LEFT_RIGHT).save('mario_horizontal_flip.png')
mario.transpose(Image.FLIP_TOP_BOTTOM).save('mario_vertical_flip.png')
print('Images flipped horizontally and vertically')


