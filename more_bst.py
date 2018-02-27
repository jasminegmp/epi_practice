class BinaryTreeNode:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
	def get_node(self):
		return self.data
	def get_left(self):
		return self.left
	def get_right(self):
		return self.right

def bst_insert(root, node):
	# Insert the main root itself
	if root.data == None:
		root = node

	# Go left
	if root.data > node.data:
		# found the leaf
		if root.left == None:
			root.left = node
		# have not found leaf
		else:
			bst_insert(root.left,node)
	# Go right
	else:
		# found the leaf
		if root.right == None:
			root.right = node
		# have not found leaf
		else:
			bst_insert(root.right,node)

def inorder(tree):
	if tree != None:
		inorder(tree.get_left())
		print(tree.get_node())
		inorder(tree.get_right())

def postorder(tree):
	if tree != None:
		postorder(tree.get_left())
		postorder(tree.get_right())
		print(tree.get_node())

def create_tree(array):
	tree = BinaryTreeNode(20)
	for i in array:
		bst_insert(tree, BinaryTreeNode(i))	
	return tree	

array = [1,5,10,12,24,25,37,57]
tree = create_tree(array)

postorder(tree)

