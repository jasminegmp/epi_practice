# STRING TIPS
# Easier to traverse from the back

# problem 6.1

def str2num(a):
	num, sign, count = 0, 1, len(a)-1
	if a[0] == '-': # Means it's negative
		sign = -1
		count -= 1
	for i in a[::-1]:
		if i != '-':
			temp = ord(i)- ord('0')
			num = (10**count)*temp + num
			count -= 1
	return sign*num
#print(str2num("-28471"))

def num2str(n):
	output_str = ''
	sign = ''
	if n < 0:
		sign = '-'
		n *= -1
	while n:
		last_dig = n % 10 # This gets the last number
		output_str = output_str + chr(ord('0') +last_dig) 
		print(output_str)
		n = n // 10 # This essentially rounds when it divides
	return sign + output_str
print(num2str(-123))

