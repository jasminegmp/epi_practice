import re

class BinaryTreeNode:
	def __init__(self, data=None, height=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
	def get_left_child(self):
		return self.left
	def get_right_child(self):
		return self.right
	def get_node(self):
		return self.data

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

def create_bst(tree, keys):
	for key in keys:
		bst_insert(tree, BinaryTreeNode(key))

def read_entire_file(text_file):
	with open(text_file, 'rt') as f:
		data = f.read()
	return data

def read_file_line_by_line(text_file):
	data = []
	with open(text_file, 'rt') as f:
		for line in f:
			temp = re.sub(r'\n', '', line) # Remove all new lines
			temp = re.split(r'\t+', temp) # Split by tabs
			data.append(temp)
	return data

def split_string(n):
	split_list = []
	for i in range(0,len(str_txt), n):
		split_list.append(int(str_txt[i:i+n]))
	return split_list

def txt_to_tree():
	n = 3
	str_txt = read_entire_file('wall_of_nums.txt')
	tree_list = split_string(n)
	tree = BinaryTreeNode(tree_list[0])
	create_bst(tree,tree_list[1:])
	inorder_traversal(tree)

text_file = 'wikicfp_crawl.txt'
cfp_list = read_file_line_by_line(text_file)
print(cfp_list)