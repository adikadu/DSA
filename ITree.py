class Tree:

	def __init__(self):
		self.root = None
		self.length = 0

	# Creates a new tree node
	def node(self, value):
		return {
		"value": value,
		"left": None,
		"right": None
		}

	# Traverses the tree using breadth first search.
	def traverse(self, value="!!"):
		if not self.root:
			print("Tree is empty...")
			return
		
		if value == "!!":
			x = []
			x.append(self.root)
			while x:
				y = x.pop(0)
				if y["left"]: x.append(y["left"])
				if y["right"]: x.append(y["right"])
				print(y["value"], end=" ")
			print()
			return

		x=[]
		x.append(self.root)
		while x:
			y=x.pop(0)
			if not y["left"] and not y["right"]:
				return y
			if value<=y["value"]:
				if y["left"]: x.append(y["left"])
				else: return y
			else:
				if y["right"]: x.append(y["right"])
				else: return y 



	# Finds the in order successor of the node
	def inord(self, start):
		if not start["left"]: return start
		return self.inord(start["left"])

	# Insert a node in the tree
	def insert(self, value):
		node = self.node(value)
		if not self.length: self.root = node
		else: 
			x = self.traverse(value)
			if not x["left"] and value<=x["value"]: x["left"] = node
			else: x["right"] = node
		self.length += 1

	# Searches for a value in the tree
	def lookup(self, value):
		if not self.length:
			return "Tree is empty..."
		x = []
		x.append(self.root)
		while x:
			y = x.pop(0)
			if y["value"] == value: return y
			if value<=y["value"]:
				if y["left"]: x.append(y["left"])
				else: return str(value)+" does not exist in tree..."
			else:
				if y["right"]: x.append(y["right"])
				else: return str(value)+" does not exist in tree..."


	# Removes the node with given value from the tree
	def remove(self, value, start="!!"):
		if start == "!!": start=self.root
		if start == None: return start
		if value<start["value"]: start["left"] = self.remove(value, start["left"])
		elif value>start["value"]: start["right"] =  self.remove(value, start["right"])
		else:
			if not start["left"] and not start["right"]: return None
			if not start["left"]:
				start["value"] = start["right"]["value"]
				start["right"] = self.remove(start["right"]["value"], start["right"])
			elif not start["right"]:
				start["value"] = start["left"]["value"]
				start["left"] = self.remove(start["left"]["value"], start["left"])
			else:
				x = self.inord(start["right"])
				start["value"] = x["value"]
				start["right"] = self.remove(x["value"], start["right"])

		return start

	# Traverses the tree using `preorder` Depth first search
	def dfs(self, value="!!"):
		if value == "!!": value=self.root
		if not value : return
		print(value["value"] ,end=" ")
		if value["left"]: self.dfs(value["left"])
		if value["right"]: self.dfs(value["right"])
 
	# Recursive BFS
	def bfsR(self, queue):
		l = len(queue)
		if not l: return
		if queue[0] == self.root:
			print(queue[0]["value"], end=" ")
		y = queue.pop(0)
		if y["left"]: 
			print(y["left"]["value"], end=" ")
			queue.append(y["left"])
		if y["right"]:
			print(y["right"]["value"], end=" ")
			queue.append(y["right"])
		self.bfsR(queue)

	# Traverses the tree using `inorder` Depth first search
	def inorder(self, value):
		if not value : return
		self.inorder(value["left"])
		print(value["value"] ,end=" ")
		self.inorder(value["right"])

	# Traverses the tree using `postorder` Depth first search
	def postorder(self, value):
		if not value : return
		self.postorder(value["left"])
		self.postorder(value["right"])
		print(value["value"] ,end=" ")
		return

	def isBst(self):
		if not self.root: return True
		x = []
		x.append(self.root)
		while x:
			y = x.pop(0)
			if y["left"]:
				if y["left"]["value"] > y["value"]: return False 
				x.append(y["left"])
			if y["right"]:
				if y["right"]["value"] < y["value"]: return False
				x.append(y["right"])
		return True


tree = Tree()
# tree.insert(3)
# tree.insert(1)
# tree.insert(2)
# print(tree.root)
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# print(tree.root)
# print("bfs", end=": ")
# tree.traverse()
# print("preorder", end=": ")
# tree.dfs()
# print()
# tree.bfsR([tree.root])
# print()
# print("inorder", end=": ")
# tree.inorder(tree.root)
# print()
# print("postorder", end=": ")
# tree.postorder(tree.root)
# print()
# print(tree.root)
# tree.insert(1)
# print(tree.lookup(19))
# print(tree.root)
# tree.lookup()
print(tree.isBst())


