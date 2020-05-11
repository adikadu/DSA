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

	def comb(self):
		x = []
		for i in self.adjList:
			for j in self.adjList[i]:
				x.append((i, j[0], j[1]))
		return x

	def find(self, dic, x):
		if dic[x][0] == x: return x
		return self.find(dic, dic[x][0])

	def union(self, dic, a, b):
		if dic[a][1] < dic[b][1]: dic[a][0] = b
		elif dic[b][1] < dic[a][1]: dic[b][0] = a
		else:
			dic[b][0] = a
			dic[a][1] += 1


	def kruskal(self):
		if not self.adjList: return
		x = self.comb()
		y = list(self.adjList.keys())
		dic = {}
		for i in y:
			dic[i] = [i, 0]
		x = sorted(x, key=lambda m: m[2])
		wt = 0
		e = 0
		j=0
		while e < self.numver-1:
			i = x[j]
			a = self.find(dic, i[0])
			b = self.find(dic, i[1])
			if a != b:
				wt += i[2]
				print(i, end=" ")
				self.union(dic, a, b)
				e += 1
			j += 1
		print()
		print("Wt. of mst: "+str(wt))


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
myGraph.traverse()
myGraph.kruskal()
# print(myGraph.comb())
