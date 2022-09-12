import os
from PIL import Image
"""
485-491
"""

baseDIR = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset"

_dirs = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset/CamScanner2-rename/"

def load_image(_dir):
	img = Image.open(_dir)

	return img

def save_crop_images(img, number):
	dir = f"{baseDIR}/Crop/crop/"
	if not os.path.isdir(dir):
		os.mkdir(dir)
	path = f"{dir}{number}.jpg"
	img.save(path)


def crop(img, pleft=6, ptop=19.5, pright=4.5, pbottom=12.5, number=None):

	width, height = img.size
	
	left = pleft * width // 100
	top = ptop * height // 100
	right = width - pright * width // 100
	bottom = height - pbottom * height // 100
	 
	img = img.crop((left, top, right, bottom))
	save_crop_images(img, number)
	return img


def save_partition_images(img, number, level):
	dir = f"{baseDIR}/Crop/partition/"
	if not os.path.isdir(dir):
		os.mkdir(dir)
	path = f"{dir}{number}_{level}.jpg"
	img.save(path)


def partion_image(img, ratio=1/44.0, n=5, number=None):
	images = []
	srt = 0
	width, height = img.size
	space = ratio*height
	size = (height - space*(n-1)) // n
	threshold = 0.2 * space
	# print(height, ratio, space,size)
	for i in range(n):
		_img = img.crop((0, srt, width, srt+size - threshold))
		if i == n - 1:
			_img = img.crop((0, srt, width, height))
		images.append(_img)

		srt += size+space
		save_partition_images(_img, number, i+1)
	return images

def extract_numbers(img):
	width, height = img.size
	sizex = width // 10
	sizey = height // 2

	numbers = []
	SHIFTX = 5
	SHIFTY = 5
	srty = 0 
	for y in range(2):
		srtx = 0
		for x in range(10):
			_img = img.crop((srtx + SHIFTX, srty + SHIFTY, srtx+sizex - SHIFTX, srty+sizey - SHIFTY))
			numbers.append(_img)
			srtx += sizex
		srty += sizey
	return numbers



fnames = list(range(1, 11))+list(range(20, 101, 10))+ [1000]


START4 = 485
END4 = 491

IMAGE_LIST = list(range(START4, END4 +1))
image_list = {i: _dirs + str(i) +".jpg" for i in IMAGE_LIST}
for COUNTER, img_dir in image_list.items():
	img = crop(load_image(img_dir), number=COUNTER)
	images = partion_image(img, number=COUNTER)
	for c, im in enumerate(images):
		nums = extract_numbers(im)
		for i, im in enumerate(nums):
			curr = f"{baseDIR}/Digits/{fnames[i]}/"
			if not os.path.isdir(curr):
				os.mkdir(curr)
			im.save(f"{curr}{COUNTER}_{c+1}.jpg")
        


