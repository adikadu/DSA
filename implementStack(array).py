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



stack = Stack()
stack.push(1)
# stack.traverse()
stack.push(2)
stack.push(3)
print("before", end=" ")
stack.traverse()
# stack.pop()
# stack.traverse()
# stack.pop()
# stack.traverse()
# print(stack.isEmpty())
# stack.pop()
# stack.pop()
# stack.traverse()
# print(stack.isEmpty())
stack.reverse()
# print(stack.arr)
print("after", end=" ")
stack.traverse()
