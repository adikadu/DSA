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
	def addEdge(self, v1, v2):
		if v1 not in self.adjList:
			print(str(v1)+" does not exist in graph...")
			return
		if v2 not in self.adjList:
			print(str(v2)+" does not exist in graph...")
			return
		# if v1 in self.adjList[v2]:
			# print("Edge "+str(v1)+"->"+str(v2)+" already exist...")
		self.adjList[v1].append(v2)
		# self.adjList[v2].append(v1)
		self.numedge += 1

	# Traverse the gaph
	def traverse(self):
		if not self.numver:
			print("Graph is empty")
		for ver in self.adjList:
			print(ver, end="-->")
			for x in self.adjList[ver][:-1]:
				print(x, end=" ")
			print(self.adjList[ver][-1])

	# Helper function for `Gbfs`
	def bfs(self, node, track):
		x=[]
		x.append(node)
		if track[node][0] == False:
			print(node, end=" ")
			track[node][0] = True
		while x:
			y = x.pop(0)
			z = self.adjList[y]
			for i in z:
				if track[i][0] == False:
					print(i, end=" ")
					track[i][0] = True
					x.append(i)
		return track

	# Helper function for `Gdfs`
	def dfs(self, node, track):

		if track[node][0] == False:
			print(node, end=" ")
			track[node][0] = True
		x = self.adjList[node]
		for i in x:
			if track[i][0] == False:
				print(i, end=" ")
				track[i][0] = True
				track=self.dfs(i, track)
		return track


	# Do the `Breadth first traversal` of graph
	def Gbfs(self, s):
		if not self.adjList: return
		x = list(self.adjList.keys())
		x.remove(s)
		x.insert(0, s)
		track = {}
		for i in x:
			track[i] = [False, False]
		for i in x:
			if track[i][1] == False:
				track = self.bfs(i, track)
		print()

	# Do the `Deapth first traversal` of graph
	def Gdfs(self, s):
		if not self.adjList: return
		x = list(self.adjList.keys())
		x.remove(s)
		x.insert(0, s)
		track = {}
		for i in x:
			track[i] = [False, False]
		for i in x:
			if track[i][1] == False:
				track = self.dfs(i, track)
		print()
		

			




myGraph = Graph()

myGraph.addVertex(0)
# myGraph.addEdge(0, 0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
# myGraph.addEdge(0, 2)
myGraph.addEdge(0, 1) 
myGraph.addEdge(0, 2) 
myGraph.addEdge(1, 2) 
myGraph.addEdge(2, 0) 
myGraph.addEdge(2, 3) 
myGraph.addEdge(3, 3) 
# myGraph.addEdge(2, 1)
# myGraph.addEdge(1, 2) 
# myGraph.addEdge(2, 0) 
# myGraph.addEdge(2, 3)
# myGraph.addEdge(3, 3)
# myGraph.addVertex(3)
# myGraph.addVertex(4)
# myGraph.addVertex(5)
# myGraph.addVertex(6)
# myGraph.addEdge(0, 1)
# myGraph.addEdge(1, 2)
# myGraph.addEdge(3, 1) 
# myGraph.addEdge(3, 4) 
# myGraph.addEdge(4, 2) 
# myGraph.addEdge(4, 5) 
# myGraph.addEdge(1, 2) 
# myGraph.addEdge(1, 0) 
# myGraph.addEdge(0, 2) 
# myGraph.addEdge(6, 5)
# print(myGraph.adjList)
print("Deapth first traversal of given graph is:",end=" ")
myGraph.Gdfs(2)
# myGraph.Gbfs(2)
# myGraph.traverse()


