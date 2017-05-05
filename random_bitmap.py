# Task 1: An RGB bitmap picture of 128x128 pixels. (70 points)
from pylab import imshow, savefig, get_cmap, axis
import requests

def get_random_float(size):
	'''
	This function gets a list of random float numbers between (0, 1)
	Because of random.org limitation, we get 10,000 numbers in each request
	'''
	nums = []
	for i in range(size/10000 + 1):
		count = min(size, (i+1)*10000) - i*10000
		r = requests.get('https://www.random.org/decimal-fractions/?num='+str(count)+'&dec=10&col=2&format=plain&rnd=new')
		nums.extend([float(f) for f in r.text.split()])
	return nums

im_size = 128		# required size of bitmap
rand_nums = get_random_float(im_size*im_size)
## Z is a im_size * im_size matrix version of the random float numbers
Z = [[rand_nums[i+im_size*j] for i in range(im_size)] for j in range(im_size)]

imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
axis('off')
savefig('random.png', bbox_inches='tight')