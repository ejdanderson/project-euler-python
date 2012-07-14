import math
def is_palindrome(num) :
	num_str = str(num)
	str_len = len(num_str)
	str_left = num_str[0:int(str_len/2)]
	str_right = num_str[int(math.ceil(float(str_len)/2)):str_len]
	str_right = str_right[::-1]
	print str_left
	print str_right
	if str_right == str_left :
		return True
	return False

start = 10
end = 999 
highest = 0

for x in range(start, end) :
	x_str = str(x)
	# If parity odd, drop middle and flip
	pali_right = x_str[0:-1]
	palindrome_low = int(x_str + pali_right[::-1])
	palindrome_high = int(x_str + x_str[::-1])

	for three_digit in range(100, 999) :
		if palindrome_high > highest and palindrome_high % three_digit == 0 and len(str(palindrome_high/three_digit)) == 3:
			highest = palindrome_high
		elif palindrome_low > highest and palindrome_low % three_digit == 0 and len(str(palindrome_low/three_digit)) == 3:
			highest = palindrome_low

print highest