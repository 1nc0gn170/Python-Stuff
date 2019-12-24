#!/usr/bin/python3

from PIL import Image
import string
import argparse


class ZSTEG():

	def __init__(self, arg_img):
		super(ZSTEG, self).__init__()
		self.pic = arg_img
		self.img_instance = Image.open(self.pic)


	def b_lsb(self):
		b_lsb_data = ""
		final_lsb_data = ""

		b_data = list(self.img_instance.getdata())
		for pixel in b_data:
			b_lsb_data+=bin(pixel[2])[-1] 

		b_plain_data = [chr(int(b_lsb_data[pixel:pixel+8],2)) for pixel in range(0,len(b_lsb_data),8)]

		for pixel in b_plain_data:
			if pixel in string.printable:
				final_lsb_data+=pixel
		return ("B DATA :\t"+final_lsb_data)

	def g_lsb(self):
		g_lsb_data = ""
		final_lsb_data = ""

		g_data = list(self.img_instance.getdata())
		for pixel in g_data:
			g_lsb_data+=bin(pixel[1])[-1] 

		g_plain_data = [chr(int(g_lsb_data[pixel:pixel+8],2)) for pixel in range(0,len(g_lsb_data),8)]

		for pixel in g_plain_data:
			if pixel in string.printable:
				final_lsb_data+=pixel

		print (self.b_lsb())
		return ("G DATA :\t"+final_lsb_data)

	def r_lsb(self):

		r_lsb_data = ""
		final_lsb_data = ""

		r_data = list(self.img_instance.getdata())
		for pixel in r_data:
			r_lsb_data+=bin(pixel[0])[-1] 

		r_plain_data = [chr(int(r_lsb_data[pixel:pixel+8],2)) for pixel in range(0,len(r_lsb_data),8)]

		for pixel in r_plain_data:
			if pixel in string.printable:
				final_lsb_data+=pixel

		print (self.g_lsb())
		return ("\nR DATA :\t"+final_lsb_data)

	def rgb_lsb(self):
		if (self.img_instance.mode != "RGB"):
			try:
				self.img_instance = self.img_instance.convert("RGB")
			except:
				print("Error Occured! Failed To Convert Into RGB")
				return
		rgb_lsb_data = ""
		final_lsb_data = ""
		rgb_data = list(self.img_instance.getdata())

		for pixel in rgb_data:
			for value in pixel:
				rgb_lsb_data+=bin(value)[-1] 

		rgb_plain_data = [chr(int(rgb_lsb_data[pixel:pixel+8],2)) for pixel in range(0,len(rgb_lsb_data),8)]
		for pixel in rgb_plain_data:
			if pixel in string.printable:
				final_lsb_data+=pixel

		print (self.r_lsb())
		return ("RGB DATA :\t"+final_lsb_data)
	
	def rgba_lsb(self):

		rgba_lsb_data = ""
		final_lsb_data = ""
		rgba_data = list(self.img_instance.getdata())

		for pixel in rgba_data:
			for value in pixel:
				rgba_lsb_data+=bin(value)[-1] 
		rgba_plain_data = [chr(int(rgba_lsb_data[pixel:pixel+8],2)) for pixel in range(0,len(rgba_lsb_data),8)]

		for pixel in rgba_plain_data:
			if pixel in string.printable:
				final_lsb_data+=pixel
		print (self.rgb_lsb())
		return "RGBA DATA :\t"+final_lsb_data

if __name__ == '__main__':
	arguments = argparse.ArgumentParser(description="Least Significant Bit Steganography finding tool")
	arguments.add_argument("-i", "--input", required=True,help="Input Image")
	arg =vars(arguments.parse_args())
	steg = ZSTEG(arg['input'])
	print(steg.rgba_lsb())
