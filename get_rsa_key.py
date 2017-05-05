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
		p = random.randint(2**(bits/2-2), 2**(bits/2))
		q = random.randint(2**(bits/2-2), 2**(bits/2))
		p += not(p&1)	# changes the values from even to odd
		q += not(q&1)

		# while not is_prime(p):
		# 	p -= 2
		# while not is_prime(q):
		# 	q -= 2
	print type(p)        

    n = p * q   
    tot = (p-1) * (q-1)
    e = tot
    while gcd(tot,e) != 1:
        e = random.randint(3,tot-1)
    d = getd(tot,e)                       # gets the multiplicative inverse
    while d<0:                            # i can probably replace this with mod
        d = d + tot
    return e,d,n

gen_key(1024)