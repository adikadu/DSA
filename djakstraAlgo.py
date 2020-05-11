class Graph:
	def __init__(self):
		self.numvar = 0
		self.numedge = 0
		self.adjList = {}

	# Add a vertex to graph(adjacency list)
	def addVertex(self, ver):
		if ver in self.adjList:
			print(str(ver)+" already exist in graph...")
			return
		self.adjList[ver] = []
		self.numvar += 1

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
		if wt < 0: print("Graph has negative weight edges so djakstra's algo may not give correct result...")
		self.adjList[v1].append((v2, wt))
		# self.adjList[v2].append((v1, wt))
		self.numedge += 1

	# Traverse the gaph
	def traverse(self):
		if not self.numvar: print("Graph is empty")
		for ver in self.adjList:
			print(ver, end="--> ")
			if self.adjList[ver]:
				for x in self.adjList[ver][:-1]:
					print(x, end=" ")
				print(self.adjList[ver][-1])
			else: print("()")

	def djakstra(self, s):
		if not self.adjList: return

		x = list(self.adjList.keys())
		dic = {}
		result = {}
		result[s] = (s, 0)

		for i in x:
			dic[i] = float("inf")
		dic[s] = 0
		e = 0
		while e < self.numvar:
			j = min(dic.values())
			minvar = [k for k in dic if dic[k] == j]
			for m in minvar:
				for i in self.adjList[m]:
					if i[0] in dic and dic[i[0]] > j+i[1]:
						dic[i[0]] =  j+i[1]
						result[i[0]] = (m, dic[i[0]])
				dic.pop(m)
				e += 1

		print(result)

myGraph = Graph()
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addVertex(4)
# myGraph.addEdge(0, 1, 10) 
# myGraph.addEdge(0, 2, 6) 
# myGraph.addEdge(0, 3, 5) 
# myGraph.addEdge(1, 3, 4) 
# myGraph.addEdge(2, 3, 4)
# myGraph.traverse()
myGraph.addEdge(0, 1, -1)  
myGraph.addEdge(0, 2, 4)  
myGraph.addEdge(1, 2, 3)  
myGraph.addEdge(1, 3, 2)  
myGraph.addEdge(1, 4, 2)  
myGraph.addEdge(3, 2, 5)  
myGraph.addEdge(3, 1, 1)  
myGraph.addEdge(4, 3, -3)
myGraph.djakstra(0)
