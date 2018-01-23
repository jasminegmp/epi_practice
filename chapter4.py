# Problem 4.1
# Compute parity of the word
# O(n) solution
# Assumption, number (num) comes in as an int/decimal
def parity(num):
	parity_sum = 0
	while num:
		if num & 1:
			parity_sum += 1
		num >>= 1
	if parity_sum % 2: # ODD
		return 1
	else:
		return 0
print(parity(3))

# Variation 2, using XOR still O(n)
def parity_2(num):
	parity_result = 0
	while num:
		parity_result ^= num & 1
		num >>= 1
	return parity_result
print(parity_2(3))

# Variation 3, O(k) where k = number of 1's
def parity_3(num):
	parity_result = 0
	while num:
		num = num & (num - 1)
		parity_result ^= 1 # Flip every time
	return parity_result
print(parity_3(3))

# problem 4.7
def power(base,exponent):
	if exponent == 1:
		return base
	return base*power(base,exponent-1)
print(power(2,15))

#problem 4.8
def reverse_digits(num):
	rev_num, temp_num = 0,0
	while num:
		rev_num = rev_num * 10
		temp_num = (num % 10) # Gets least significant digit
		num = (num - temp_num)/10
		rev_num += temp_num
	return rev_num
print(reverse_digits(3741923))

