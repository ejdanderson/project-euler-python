import math
sum = 0
square_sum = 0
for x in range(1, 101) :
	sum += x
	square_sum += x*x
sum_sq = sum * sum

print sum_sq - square_sum
	

