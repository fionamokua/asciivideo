#import all the necessary libraries
import cv2
import sys
from PIL import Image
#the ascii characters intended to be used in the image conversion
ASCII_CHARACTERS=["@","#","~","S","%","?","*","+",";",":",",","."]
#function to resize and grayscale an image
def resized_gray_image(image,new_width=70):
	width,height=image.size
	aspect_ratio=height/width
	new_height=int(aspect_ratio*new_width)
	resized_gray_image=image.resize((new_width,new_height)).convert("L")
	return resized_gray_image
def pix2chars(image):
	pixels=image.getdata()
	characters="".join([ASCII_CHARACTERS[pixel//25] for pixel in pixels])
	return characters
def generate_frame(image,new_width=70):
	new_image_data=pix2chars(resized_gray_image(image))
	total_pixels=len(new_image_data)
	ascii_image="/n" .join ([new_image_data[index:(index+new_width)] for index in range(0,total_pixels,new_width)])
	sys.stdout.write(ascii_image)
	os.system("cls" if os.name=='nt' else 'clear')

cap=cv2.VideoCapture("logan.mp4")

while True:
	ret,frame=cap.read()
	cv2.imshow("frame",frame)
	generate_frame(Image.fromarray(frame))
	cv2.waitkey(1)

