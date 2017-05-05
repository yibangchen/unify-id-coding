# Task2: A white noise WAV sound sample of 3 seconds (70 points)
import struct
import wave
import requests

def get_randint(size, min_bound, max_bound):
	'''
	This function gets a list of random int numbers between (min_bound, max_bound)
	Because of random.org limitation, we get 10,000 numbers in each request
	'''
	nums = []
	for i in range(size/10000 + 1):
		count = min(size, (i+1)*10000) - i*10000
		r = requests.get('https://www.random.org/integers/?num='+str(count)+'&min='+str(min_bound)+'&max='+str(max_bound)+'&col=5&base=10&format=plain&rnd=new')
		nums.extend([float(f) for f in r.text.split()])
	return nums

NOISE_LEN = 44100 * 3 	# count of random numbers to generate 3-second wav file
MIN_BOUND = -32767
MAX_BOUND = 32767
rand_noise = wave.open('random.wav', 'w')
rand_noise.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

rand_nums = get_randint(NOISE_LEN, MIN_BOUND, MAX_BOUND)
values = []
for n in rand_nums:
    packed_n = struct.pack('h', n)
    values.append(packed_n)
    values.append(packed_n)

rand_noise.writeframes(''.join(values))
rand_noise.close()