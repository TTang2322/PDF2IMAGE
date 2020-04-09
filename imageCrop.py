#!/usr/bin/python3

from PIL import Image

def imageCrop(arg_image_path,arg_image_cropped_path):
	image_path=arg_image_path
	image_cropped_path=arg_image_cropped_path

	im=Image.open(image_path)

	img_size=im.size
	print("width and height of image are {}".format(img_size))

	x,y,w,h=100,100,250,250

	region=im.crop((x,y,x+w,y+h))

	region.save(image_cropped_path)

	print("crop is done")

if __name__ == '__main__':
	image_path="/Users/ttang/Desktop/pdf2image/Sample/Sample_resized-0.jpeg"
	image_cropped_path="/Users/ttang/Desktop/pdf2image/CroppedImage/Sample_resized-0-cropped.jpeg"
	imageCrop(image_path,image_cropped_path)