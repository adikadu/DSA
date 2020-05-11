class Stack:
	def __init__(self):
		self.arr = []
	def peek(self):
		if not self.arr:
			print("Stack is empty!!!")
			return
		return self.arr[len(self.arr)-1]
	def push(self, value): self.arr.append(value)
	def pop(self):
		if not self.arr:
			print("Stack is empty!!!")
			return
		return self.arr.pop()
	def isEmpty(self):
		return not bool(self.arr)
	def traverse(self):
		if not self.arr:
			print("Stack is empty!!!")
			return
		for i in self.arr:
			print(i)
	def reverse(self):
		if not self.arr:
			print("Stack is empty!!!")
			return
		self.arr.reverse()

class Queue:
	def __init__(self):
		self.stack = Stack()
	def peek(self):
		if self.stack.isEmpty():
			print("Queue is empty...")
			return
		return self.stack.peek()
	def enqueue(self, value):
		if self.stack.isEmpty():
			self.stack.push(value)
			return
		self.stack.reverse()
		self.stack.push(value)
		self.stack.reverse()
	def dequeue(self):
		if self.stack.isEmpty():
			print("Queue is empty...")
			return
		self.stack.pop()
	def isEmpty(self):
		return self.stack.isEmpty()
	def traverse(self):
		if self.stack.isEmpty():
			print("Queue is empty...")
			return
		self.stack.traverse()

q = Queue()
print(q.isEmpty())
q.peek()
q.traverse()
q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.isEmpty())
q.dequeue()
print(q.peek())
print("before dequeue")
q.traverse()
q.dequeue()
print("after dequeue")
q.traverse()
