import math
def half_pi(n):
	pi = 0
	frac = 1/n
	for i in range(1,n):
		pi += math.sqrt(i*frac*(1-i*frac))*frac
	return pi*8

print (half_pi(90000009))