import math
def is_prime(num) :
	for x in range(2, int(math.sqrt(num))) : 
		if num % x == 0 :
			return False
	return True

def get_prime_factors(num) :
	for x in range (3, int(math.sqrt(num))) :
		
		if num % x == 0  and is_prime(x) :
			print x
			right_factor = num/x
			if ( is_prime(right_factor)) :
				print right_factor
get_prime_factors(600851475143)
