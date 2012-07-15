found = False
num = 20
while not found :
	#assume this num is the correct one
	found = True
	# 10 - 1 will have multiples from 20 to 11
	for x in range(19, 10, -1) :
		print x
		if num % x != 0 :
			found = False
			num += 20
			break;

print num
