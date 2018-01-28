class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
	def get_left_child(self):
		return self.left
	def get_right_child(self):
		return self.right
	def set_node(self, data):
		self.data = data
	def get_node(self):
		return self.data
	def insert_left_child(self, node):
		if self.left == None:
			self.left = Node(node)
		else:
			tree = Node(node)
			self.left = tree
			tree.left = self.left
	def insert_right_child(self, node):
		if self.right == None:
			self.right = Node(node)
		else:
			tree = Node(node)
			self.right = tree
			tree.right = self.right

def bst_insert(root, node):
	if root is None:
		root = node
	else:
		if root.data > node.data:
			if root.left is None:
				root.left = node
			else:
				bst_insert(root.left, node)
		else:
			if root.right is None:
				root.right = node
			else:
				bst_insert(root.right, node)

def inorder_traversal(tree):
	if tree != None:
		inorder_traversal(tree.get_left_child())
		print(tree.get_node())
		inorder_traversal(tree.get_right_child())

def preorder_traversal(tree):
	if tree !=None:
		print(tree.get_node())
		preorder_traversal(tree.get_left_child())
		preorder_traversal(tree.get_right_child())

def postorder_traversal(tree):
	if tree != None:
		postorder_traversal(tree.get_left_child())
		postorder_traversal(tree.get_right_child())
		print(tree.get_node())

def create_bst(tree, data):
	for item in data:
		bst_insert(tree, Node(item))
	return tree

tree = Node(200)
data = [100,75,150,25,80,125,175,1,30,400,250,300,350,500]
tree = create_bst(tree, data)

print("------------")

print("In order")
inorder_traversal(tree)
print("------------")

print("Pre order")
preorder_traversal(tree)
print("------------")

print("Post order")
postorder_traversal(tree)
print("------------")

