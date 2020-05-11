class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0

	def node(self, value):
		return {
		"value": value,
		"next": None
		}

	def peek(self):
		if not self.length: return "Stack is empty!!!"
		return self.top["value"]

	def push(self, value):
		node = self.node(value)
		node["next"] = self.top
		self.top = node
		if not self.length: self.bottom = node
		self.length+=1

	def pop(self):
		if not self.length:
			print("Stack is empty!!!")
			return
		node = self.top
		if self.length==1:
			self.top = None
			self.bottom = None
		else: self.top = self.top["next"]
		self.length -= 1
		node["next"] = None
		return node

	def isEmpty(self):
		return not bool(self.length)

	def traverse(self):
		if not self.length:
			print("Stack is empty!!!") 
			return 
		x = self.top
		for i in range(self.length):
			print(x["value"])
			x = x["next"]


stack = Stack()
print("Empty:",end=" ")
stack.traverse()
stack.push(1)
stack.push(2)
stack.push(3)
print("Three values:", end=" ")
stack.traverse()
print("peek=", end=" ")
print(stack.peek())
stack.pop()
print("Two values:", end=" ")
stack.traverse()
print("peek=", end=" ")
print(stack.peek())

