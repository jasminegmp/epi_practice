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