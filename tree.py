class BinaryTreeNode:
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
	if tree is not None:
		inorder_traversal(tree.get_left_child())
		print(tree.get_node())
		inorder_traversal(tree.get_right_child())

def preorder_traversal(tree):
	if tree is not None:
		print(tree.get_node())
		inorder_traversal(tree.get_left_child())
		inorder_traversal(tree.get_right_child())

def postorder_traversal(tree):
	if tree is not None:
		inorder_traversal(tree.get_left_child())
		inorder_traversal(tree.get_right_child())
		print(tree.get_node())

tree = BinaryTreeNode(8)
keys = [4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

for key in keys:
	bst_insert(tree, BinaryTreeNode(key))
inorder_traversal(tree)


