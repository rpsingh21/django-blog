import datetime
import math
import re
import os,sys
from PIL import Image

from django.utils.html import strip_tags


def count_words(html_string):
	word_string = strip_tags(html_string)
	matching_words = re.findall(r'\w+', word_string)
	count = len(matching_words)
	return count

def get_read_time(html_string):
	count = count_words(html_string)
	read_time_min = math.ceil(count/120.0) 
	return int(read_time_min)

def conv_thumbnail(image,size):
	img = Image.open(image.path)
	img.thumbnail(size,Image.ANTIALIAS)
	img.save(image.path,img.format,quality=0)
	image=img
	return image