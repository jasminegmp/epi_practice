# Chapter 5
# Problem 5.1 - dutch flag partition
def dutch_flag_partition(A, index):
	pivot = A[index]
	print("pivot:", pivot)

	# remove pivot from A
	del A[index]
	pivot_index = 0
	i = 0;

	for j in range(len(A)):
		if A[j] < pivot:
			# Swap i and j
			temp = A[j]
			A[j] = A[i]
			A[i] = temp
			i += 1
	A.insert(i, pivot)
	return A

print(dutch_flag_partition([7,2,1,8,6,3,5,4], 4))

# problem 5.6 buy and sell a stock once - O(N)
def optimize_buy_sell(s_array):
	current_max, buy = 0, 0;
	for sell in s_array:
		print(sell,s_array[buy])
		if sell > buy:
			difference = sell - s_array[buy]
			if difference >= 0:
				if current_max < difference:
					current_max, high, low = difference, sell, s_array[buy]
			else:
				buy += 1
	return current_max, low, high

print(optimize_buy_sell([310,315,275,295,260,270,290,230,255,250]))