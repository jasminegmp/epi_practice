class Stack:
	def __init__(self,data=0):
		self.stack = []
	def push(self, data=0):
		return self.stack.append(data)
	def pop(self):
		return self.stack.pop()
	def is_empty(self):
		return (len(self.stack) == 0)
	def print(self):
		print(self.stack)

	# problem 8.1 - O(N)
	def find_max(self):
		stack = self.stack
		stack_max = stack[0]
		for i in range((len(stack)-1)):
			#print(stack[i])
			if stack[i] < stack[i+1]:
				stack_max = stack[i+1]
		return stack_max

def test_8p1():
	s = Stack()
	s.push(10)
	s.push(2)
	s.push(1)
	s.push(1)
	s.push(20)
	s.push(1)
	s.print()
	print(s.find_max())

class Queue:
	def __init__(self):
		self.queue = []
	def enqueue(self,data=0):
		return self.queue.append(data)
	def dequeue(self):
		return self.queue.pop(0)
	def is_empty(self):
		return (len(self.queue) == 0)
	def print(self):
		print(self.queue)

class CircularQueue:
	def __init__(self, max_capacity):
		self.queue = [None]*max_capacity
		self.max_capacity = max_capacity
		self.start = 0
		self.end = 0
	def enqueue(self,data=0):
		print("@", print(self.queue))
		if (self.end - self.start) == self.max_capacity:
			self.end = 0
			print("!", print(self.queue))
		if not self.is_empty:
			if (self.start == self.end):
				self.start = self.start + 1
		self.queue[self.end] = data
		self.end = self.end + 1
		return self
	def dequeue(self):
		if self.start > self.max_capacity - 1:
			self.start = 0
		else:
			self.end = self.max_capacity - 1
		return self.queue.pop(self.end)
	def is_empty(self):
		return (len(self.queue) == 0)
	def print(self):
		print(self.queue)

def test_8p7():
	w = CircularQueue(4)
	w.enqueue(2)
	w.enqueue(4)
	w.enqueue(7)
	w.enqueue(8)
	w.enqueue(1)
	w.enqueue(6)
	w.print()
	w.dequeue()
	w.print()
	print(w.is_empty())

#test_8p1()
test_8p7()


