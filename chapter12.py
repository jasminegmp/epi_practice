import collections
# problem 12.1 Palindrome
def palindrome(s):
	sum = 0
	for i in collections.Counter(s).values():
		sum += (i%2)
		if sum <= 1:
			output = True
		else:
			output = False
	return output

print(palindrome('level'))
