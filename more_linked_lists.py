class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self,head):
		self.head = head

def insert_head(data, ll):
	node = Node(data)
	node.next = ll.head
	ll.head = node

def insert_tail(data, ll):
	current = ll.head
	node = Node(data)
	print("current", current, "node.data",node.data)
	if current != None:
		while current.next != None:
			current = current.next
		temp_next = current.next
		current.next = node
		current = node
		current.next = temp_next
		current = current.next
	else:
		current = node
	print("!!!!!!ll", current.data)

def insert_index(index, data, ll):
	node = Node(data)
	current = ll.head
	i = 0
	while current:
		if i == index:
			temp_next = current.next
			current.next = node
			current = node
			current.next = temp_next
		current = current.next
		i += 1

def delete_head(ll):
	current = ll.head
	ll.head = current.next
	current.next = None

def search(key,ll):
	current = ll.head
	while current:
		if current.data == key:
			print(current.data)
		current = current.next

def print_ll(ll):
	current = ll.head
	while current:
		print (current.data)
		current = current.next

def merge(ll1,ll2):
	ll3 = LinkedList(None)
	ll1_current = ll1.head
	ll2_current = ll2.head
	while ll1_current and ll2_current:
		print("ll1",ll1_current.data, "ll2", ll2_current.data)
		if ll1_current.data < ll2_current.data:
			insert_tail(ll1_current.data, ll3)
			ll1_current = ll1_current.next
		else:
			insert_tail(ll2_current.data,ll3)
			ll2_current = ll2_current.next

		print("ll3")
		print_ll(ll3)
	if ll1_current:
		print("still have ll1 left")

	if ll2_current:
		print("still have ll2 left")
	return ll3

ll1 = LinkedList(Node(7))
insert_head(5,ll1)
insert_head(2,ll1)
#insert_index(1, 2, ll)
print_ll(ll1)
print("________")


ll2 = LinkedList(Node(11))
insert_head(3,ll2)
insert_tail(13,ll2)
print_ll(ll2)
print("________")


ll3 = merge(ll1,ll2)

print_ll(ll3)
