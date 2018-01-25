import linked_list

# problem 7.1
def merge_two_sorted_lists(ll1, ll2):
	ll1 = ll1.head
	ll2 = ll2.head
	output = linked_list.LinkedList()
	while ll1 and ll2:
		if ll1.data < ll2.data:
			output.insert(ll1.data)
			ll1 = ll1.next
		else:
			output.insert(ll2.data)
			ll2 = ll2.next
	if ll1:
		output.insert(ll1.data)
	if ll2:
		output.insert(ll2.data)
	return output

ll1 = linked_list.LinkedList()
ll1.insert(7)
ll1.insert(5)
ll1.insert(2)

ll2 = linked_list.LinkedList()
ll2.insert(11)
ll2.insert(3)

ll1.print_nodes()
ll2.print_nodes()

output = merge_two_sorted_lists(ll1,ll2)
output.print_nodes()