class BinaryTreeNode:
	def __init__(self, data=None, height=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		self.height = height
		#print("CREATING NODE:", self.data)
	def get_left_child(self):
		return self.left
	def get_right_child(self):
		return self.right
	def set_node(self, data):
		self.data = data
	def get_node(self, height=None):
		if height != None:
			self.set_height(height)
			#print("self.data, self.height", self.data, self.height)
		return self.data
	def get_height(self):
		return self.height
	def set_height(self, height):
		self.height = height
	def insert_left_child(self, node):
		if self.left == None:
			self.left = BinaryTreeNode(node)
		else:
			self = self.left
			self.insert_left_child(node)
	def insert_right_child(self, node):
		if self.right == None:
			self.right = BinaryTreeNode(node)
		else:
			self = self.right
			self.insert_right_child(node)

def bst_insert(root, node):
	#print("INSERT")
	#print("root.data, node.data",root.data, node.data)
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


def inorder_traversal(tree):
	#print("LOOP!")
	if tree is not None:
		#print("Direction", direction)
		#print("Tree.get_node()", tree.get_node())
		#print("Tree.get_left_child()", tree.get_left_child())
		#print("Tree.get_right_child()", tree.get_right_child())
		#print(" ")
		inorder_traversal(tree.get_left_child())
		print(tree.get_node())
		#print(" ")
		inorder_traversal(tree.get_right_child())

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

def get_left_height(tree):
	if tree is not None:
		height = get_left_height(tree.get_left_child())
		return height + 1
	else:
		return 0
def get_right_height(tree):
	if tree is not None:
		height = get_right_height(tree.get_right_child())
		return height + 1
	else:
		return 0

# Problem 9.1 check if tree is balanced
def height_balanced(tree, height, root):
	# Do post order tree traversal
	output = True
	if tree is not None:
		height += 1
		height_balanced(tree.get_left_child(), height, root)
		height_balanced(tree.get_right_child(), height, root)
		print(tree.get_node(height))
		current_tree_height = tree.get_height()
		if (tree.get_left_child() != None) and (tree.get_right_child() != None):
			print("child height LEFT",get_left_height(tree.get_left_child()))
			left_subtree_height = get_left_height(tree.get_left_child())
			print("child height RIGHT",get_right_height(tree.get_right_child()))
			right_subtree_height = get_right_height(tree.get_right_child())
			print("height diff", abs(left_subtree_height-right_subtree_height))
			if abs(left_subtree_height-right_subtree_height) > 1:
				return False
		elif (tree.get_left_child() == None) and (tree.get_right_child() != None):
			return False
		elif (tree.get_left_child() != None) and (tree.get_right_child() == None):
			return False
	return True

root = 200
tree = BinaryTreeNode(root)
keys = [100,50,1,55,150,400,300,450]
tree.insert_right_child(5000)
create_bst(tree, keys)
inorder_traversal(tree)
print(height_balanced(tree, 0, root))

