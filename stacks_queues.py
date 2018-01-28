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

def stack_test():
	s = Stack()
	s.push(10)
	s.push(2)
	s.push(1)
	s.push(1)
	s.push(20)
	s.push(1)
	s.print()
	s.pop()
	s.pop()
	s.print()
	print(s.is_empty())

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

def queue_test():
	w = Queue()
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

stack_test()
queue_test()


