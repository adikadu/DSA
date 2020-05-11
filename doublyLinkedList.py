class doublyLinkedList:

	def __init__(self, value):
		self.head = {
		"value": value,
		"next": None,
		"prev": None
		}
		self.head["next"] = self.head
		self.head["prev"] = self.head
		self.tail = self.head
		self.length = 1

	def node(self, value):
		return {
		"value": value,
		"next": None,
		"prev": None
		}

	def traverse(self, type=1):
		if not self.length:
			print("List is empty")
			return
		if type == 1:
			x = self.head
			y = self.length
			while y!=1:
				print(x["value"], end="->")
				x = x["next"]
				y-=1
			print(x["value"])

		if type == -1:
			x = self.tail
			y = self.length
			while y!=1:
				print(x["value"], end="->")
				x = x["prev"]
				y-=1
			print(x["value"])

	def append(self, value):
		x = self.node(value)
		self.tail["next"] = x
		x["prev"] = self.tail
		self.tail = x
		self.length +=1

	def prepend(self, value):
		x = self.node(value)
		x["next"] = self.head
		self.head["prev"] = x
		x["prev"] = self.tail
		self.tail["next"] = x
		self.length +=1
		self.head = x

	def insert(self, value, index):
		x = self.node(value)
		y = self.head
		for i in range(index-1):
			y = y["next"]
		x["next"] = y["next"]
		y["next"] = x
		x["prev"] = y
		x["next"]["prev"] = x
		self.length += 1

	def delete(self, index):
		y = self.head
		for i in range(index):
			y = y["next"]
		y["prev"]["next"] = y["next"]
		y["next"]["prev"] = y["prev"]
		self.length -= 1




dList = doublyLinkedList(10)
print("Length of list is", end=" ")
print(dList.length)
dList.traverse()
dList.append(11)
dList.append(12)
dList.append(13)
dList.prepend(9)
dList.insert(15, 2)
print("Length of list is", end=" ")
print(dList.length)
print("forward:", end=" ")
dList.traverse()
print("backward:", end=" ")
dList.traverse(-1)
dList.delete(2)
print("Length of list is", end=" ")
print(dList.length)
print("forward:", end=" ")
dList.traverse()
print("backward:", end=" ")
dList.traverse(-1)
