# Task3: An RSA key pair. (100 points)
import requests

def get_randint(bits):
	limbs = []		# each limb is a set of 16-bit integers to form the require bit number
	for i in range(size/10000 + 1):
		count = min(size, (i+1)*10000) - i*10000
		r = requests.get('https://www.random.org/integers/?num='+str(count)+'&min='+str(min_bound)+'&max='+str(max_bound)+'&col=5&base=10&format=plain&rnd=new')
		nums.extend([float(f) for f in r.text.split()])
	return limbs

def gen_key(bits):
	p = q = 3
	while p == q:
		p = get_randint()
		q = get_randint()

gen_key(1024)