class BinaryTreeNode:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		#print("CREATING NODE:", self.data)

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
			self.left = BinaryTreeNode(node)
		else:
			tree = BinaryTreeNode(node)
			self.left = tree
			tree.left = self.left
	def insert_right_child(self, node):
		if self.right == None:
			self.right = BinaryTreeNode(node)
		else:
			tree = BinaryTreeNode(node)
			self.right = tree
			tree.right = self.right

def bst_insert(root, node):
	print("INSERT")
	print("root.data, node.data",root.data, node.data)
	if root is None:
		root = node
	else:
		if root.data > node.data:
			#print("<<<<<<<<<<<<<")
			#print("root.data > node.data",root.data, node.data)
			#print("root.left", root.left)
			if root.left is None:
				root.left = node
			else:
				bst_insert(root.left, node)
		else:
			#print(">>>>>>>>>>>>>")
			#print("root.data < node.data",root.data, node.data)
			#print("root.right", root.right)
			if root.right is None:
				root.right = node
			else:
				bst_insert(root.right, node)


def inorder_traversal(tree, direction):
	print("LOOP!")
	if tree is not None:
		print("Direction", direction)
		print("Tree.get_node()", tree.get_node())
		print("Tree.get_left_child()", tree.get_left_child())
		print("Tree.get_right_child()", tree.get_right_child())
		print(" ")
		postorder_count(tree.get_left_child(), "left")
		print(tree.get_node())
		print(" ")
		postorder_count(tree.get_right_child(), "right")

def preorder_traversal(tree):
	if tree is not None:
		print(tree.get_node())
		preorder_traversal(tree.get_left_child())
		preorder_traversal(tree.get_right_child())

def postorder_traversal(tree):
	if tree is not None:
		postorder_traversal(tree.get_left_child())
		postorder_traversal(tree.get_right_child())
		print(tree.get_node())
def create_bst(tree, keys):
	for key in keys:
		bst_insert(tree, BinaryTreeNode(key))
		#inorder_traversal(tree, "root")

def postorder_count(tree, direction):
	if tree is not None:
		#print("Direction", direction)
		#print("Tree.get_node()", tree.get_node())
		#print("Tree.get_left_child()", tree.get_left_child())
		#print("Tree.get_right_child()", tree.get_right_child())
		postorder_count(tree.get_left_child(), "left")
		postorder_count(tree.get_right_child(), "right")
		print(tree.get_node())
	#return tree



tree = BinaryTreeNode(200)
#keys = [4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
#keys = [4, 12, 2, 6]
keys = [100,75,150,25,80,125,175,1,30,400,250,300,350,500]
create_bst(tree, keys)
postorder_count(tree, "root")

