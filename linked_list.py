class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
    	return self.data

    def get_next(self):
    	return self.next

    def set_data(self, val):
    	self.data = val

    def set_next(self, val):
    	self.next = val

class LinkedList:
    def __init__(self=None, head=None):
        self.head = head

    def insert(self, data): # Insert at head
    	new_node = Node(data, self.head)
    	self.head = new_node

    def delete(self, key): # Delete that matches key
    	current = self.head
    	#prev = current
    	while current and current.data != key:
    			prev = current
    			current = current.next
    	prev.next = current.next
    	return current

    def print_nodes(self):
    	output = []
    	arrow = "->"
    	current = self.head
    	while current:
    		output.append(str(current.data))
    		current = current.next
    	print(arrow.join(output))

    def search(self, key):
    	current = self.head
    	while current and current.data != key:
    			current = current.next
    	return current

'''
ll1 = LinkedList()
ll1.insert(1)
ll1.insert(110)
ll1.insert(20)
ll1.print_nodes()
found = ll1.search(1)
print(found.data)
ll1.delete(1)
ll1.print_nodes()

'''