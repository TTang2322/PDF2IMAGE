#!/usr/bin/python3

from wand.image import Image
import os

# convert pdf to jpeg
def pdf2im(pdf_path):
	print('============starting converting,please waiting....')
	with Image(filename=pdf_path) as img:

		print('============The total number of pages in this pdf is ', len(img.sequence))

		# get the size of image
		scale=1
		width=img.width
		height=img.height
		resized_width=int(width*scale)
		resized_height=int(height*scale)
		
		# with img.convert('jpeg') as converted:
		with img.convert('pdf') as converted:

			# resize image
			print('============The original size of image is ',converted.size)
			converted.sample(resized_width,resized_height)
			print('============The size of resized image is ',converted.size)

			# save image
			# converted.save(filename='./Construction/Construction_cropped_pt2.jpeg')
			converted.save(filename='./Construction/Construction_cropped_pt2_copy.svg')
			print('============Finished!')

if __name__ == '__main__':
	pdf2im('./Construction_cropped_pt2.pdf')
