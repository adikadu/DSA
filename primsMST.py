class Graph:
	def __init__(self):
		self.numver = 0
		self.numedge = 0
		self.adjList = {}

	# Add a vertex to graph(adjacency list)
	def addVertex(self, ver):
		if ver in self.adjList:
			print(str(ver)+" already exist in graph...")
			return
		self.adjList[ver] = []
		self.numver += 1

	# Add an edge to graph(adjacency list)
	def addEdge(self, v1, v2, wt):
		if v1 not in self.adjList:
			print(str(v1)+" does not exist in graph...")
			return
		if v2 not in self.adjList:
			print(str(v2)+" does not exist in graph...")
			return
		if v1 in self.adjList[v2]:
			print("Edge "+str(v1)+"->"+str(v2)+" already exist...")
		self.adjList[v1].append((v2, wt))
		self.adjList[v2].append((v1, wt))
		self.numedge += 1

	# Traverse the gaph
	def traverse(self):
		if not self.numver: print("Graph is empty")
		for ver in self.adjList:
			print(ver, end="--> ")
			if self.adjList[ver]:
				for x in self.adjList[ver][:-1]:
					print(x, end=" ")
				print(self.adjList[ver][-1])
			else: print("()")

	def prims(self, s):
		if not self.adjList: return
		x = list(self.adjList.keys())
		dic = {}
		for i in x:
			dic[i] = float("inf")
		dic[s] = 0
		# print(dic)
		# print()
		e = 0
		mst = 0
		while e< self.numver:
			j = min(dic.values())
			mst += j
			minKey = [k for k in dic if dic[k] == j]
			minKey = minKey[0]
			for j in self.adjList[minKey]:
				if j[0] in dic and dic[j[0]] > j[1]: dic[j[0]] = j[1]
			e += 1
			x = minKey
			dic.pop(minKey)
			# print(dic)
			# print()
			# print(x)
		print("mst: "+str(mst))



myGraph = Graph()
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addEdge(0, 1, 10) 
myGraph.addEdge(0, 2, 6) 
myGraph.addEdge(0, 3, 5) 
myGraph.addEdge(1, 3, 15) 
myGraph.addEdge(2, 3, 4)
# myGraph.traverse()
myGraph.prims(0)
# print(myGraph.adjList[0])