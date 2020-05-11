class LinkedList:
	
	# Constructor of the class
	def __init__(self, value):
		self.head = {
			"value":value,
			"next": None
		}
		self.length = 0

    # Traverse the list
	def traverse(self, index=-1):
		x = self.head
		self.length = 0
		if x:
			self.length += 1
			if index == -1:
				while x["next"]:
					self.length+=1
					print(x["value"], end="->")
					x=x["next"]
				print(x["value"])
			else:
				while index:
					x=x["next"]
					index-=1
			return x
		else: print("List is empty!!!")

    # Create a new node for list
	def node(self, value):
		return {"value": value, "next": None}
    
    # Append a node at the end of list 
	def appItem(self, value):
		x = self.head
		while x["next"]: x=x["next"]
		x["next"] = self.node(value)
		return self.head

    # Append a node at the begining of list
	def preItem(self, value):
		x = self.node(value)
		x["next"] = self.head
		self.head = x
		return self.head

    # Append a node at given index in the list
	def insert(self, value, index):
		x = self.traverse(index-1)
		y = self.node(value)
		y["next"] = x["next"]
		x["next"] = y
		return self.head

    # Delete a node at the begining of list
	def preDelete(self):
		if self.length:
			x = self.head
			self.head = self.head["next"]
			x.clear()
			self.length -=1
		else: print("List is empty!!!")

    # delete a node at the end of list 
	def postDelete(self):
		if not self.length:
			print("List is empty!!!")
			return self.head
		if self.length == 1: return self.preDelete()
		x = self.traverse(self.length-2)
		y=x["next"]
		x["next"] = None
		y.clear()
		self.length -=1
		return self.head

    # Delete a node at given index in the list
	def indDelete(self, index):
		if not self.length:
			print("List is empty!!!")
			return self.head
		if not index:  return self.preDelete()
		if index == self.length-1: return self.postDelete()
		x = self.traverse(index-1)
		x["next"] = x["next"]["next"]
		self.length -=1
    
    # Search the given value in the list
	def search(self, value):
		if self.length:
			x=self.head
			while x and x["value"] != value:
				x=x["next"]
			if not x: print("value not present in list!!!")
			else:
				print("value found!!!")
				return x
		else: print("List is empty!!!")

	def reverse(self):
		if not self.length:
			print("Liat is Empty!!!")
			return
		if self.length == 1:
			return self.head
		prev = None
		curr = self.head
		next = curr["next"]
		while next:
			curr["next"] = prev
			prev = curr
			curr = next
			next = curr["next"]
		curr["next"] = prev
		self.head = curr





		

List1 = LinkedList(10)
List1.preItem(12)
List1.appItem(13)
List1.insert(14, 2)
List1.traverse()
# print("Length of list" ,end=" ")
# print(List1.length)
# List1.preDelete()
# print("After preDelete")
# List1.traverse()
# print("Length of list" ,end=" ")
# print(List1.length)
# print("After postDelete")
# List1.postDelete()
# List1.indDelete(1)
# print(List1.search(13))
# List1.traverse()
# print("Length of list" ,end=" ")
# print(List1.length)
# print(List1.traverse(3)["value"])
List1.reverse()
List1.traverse()
List1.reverse()
List1.traverse()
