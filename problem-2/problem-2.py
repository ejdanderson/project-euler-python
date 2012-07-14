next_num = 0
cur_num = 3 
prev_1 = 2 
sum = 2


while (cur_num < 4000000):
	if cur_num % 2 == 0:
		sum += cur_num
	
	next_num = cur_num + prev_1
	prev_1 = cur_num
	cur_num = next_num
print sum
