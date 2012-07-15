import math
def is_prime(num) :
        for x in range(2, int(math.sqrt(num))+1) : 
                if num % x == 0 :
                        return False
        return True

cur_num = 1
# skip 1 and 2 so increment can be by 2
num_primes = 1
while num_primes != 10001 :
	cur_num += 2
	if is_prime(cur_num) :
		num_primes += 1
print cur_num
