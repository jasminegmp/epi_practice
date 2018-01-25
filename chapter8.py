class Stack:
	def __init__(self,data=0):
		self.stack = []
	def push(self, data=0):
		stack = self.stack
		return stack.append(data)
	def pop(self):
		stack = self.stack
		return self.stack.pop()
	def is_empty(self):
		stack = self.stack
		return (len(stack) == 0)
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

s = Stack()
s.push(10)
s.push(2)
s.push(1)
s.push(1)
s.push(20)
s.push(1)
s.print()
print(s.find_max())
