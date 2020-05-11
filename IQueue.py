class Queue:

	# Constructor of Queue
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	# Create a new node
	def node(self, value):
		return {
		"value": value,
		"next": None
		}

	# return the value of first element
	def peek(self):
		if not self.length:
			print("Queue is empty...")
			return
		return self.first["value"]

	# insert an element in queue
	def enqueue(self, value):
		node = self.node(value)
		if not self.length: 
			self.first = node
			self.last = node
		else: 
			self.last["next"] = node
			self.last = node
		self.length += 1

	# delete an element from queue 
	def dequeue(self):
		if not self.length:
			print("Queue is empty...")
			return
		node = self.first
		if self.length == 1: 
			self.first = None
			self.last = None
		else: self.first = self.first["next"]
		node["next"] = None
		self.length -= 1
		return node

	# Checks if queue is empty or not
	def isEmpty(self):
		return not bool(self.length)

	# traverse through the list
	def traverse(self):
		if not self.length:
			print("Queue is empty...")
			return
		x = self.first
		for i in range(self.length-1):
			print(x["value"], end=" ")
			x = x["next"]
		print(x["value"])


q = Queue()
print(q.isEmpty())
q.traverse()
q.enqueue(1)
q.enqueue(2)
q.traverse()
q.enqueue(3)
# print(q.first)
q.traverse()
q.dequeue()
q.traverse()
print(q.isEmpty())




