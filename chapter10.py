# Heaps
# heapq is a min heap
import heapq

def heap_test():
	l = [5,1,2,6,8,9,4]

	# Converts into heap
	# Moves smallest value to index 0
	# Only index 0 is correct
	heapq.heapify(l)
	print(l)

	# Push element 7 into heap
	heapq.heappush(l, 7)
	print(l)

	# Push element 0 into heap
	heapq.heappush(l, -1)
	print(l)

	# Remove smallest element
	heapq.heappop(l)
	print(l)

	# Push 0 into heap and return smallest element
	low = heapq.heappushpop(l, 0)
	print(l, low)

	low = l[0]
	print(low)
	print(l)

	# finds n largest
	output = heapq.nlargest(2, l)
	print(output)

	# find n smallest
	output = heapq.nsmallest(2, l)
	print(output)

# Problem 10.1
def merge_sorted_list(l):
	pop = []
	while l:
		for sorted_array in l:
			#print(sorted_array)
			if sorted_array:
				pop.append(heapq.heappop(sorted_array))
			print("sa",sorted_array)
	print(pop)


l = [[3,5,7],[0,6],[0,6,28]]
merge_sorted_list(l)